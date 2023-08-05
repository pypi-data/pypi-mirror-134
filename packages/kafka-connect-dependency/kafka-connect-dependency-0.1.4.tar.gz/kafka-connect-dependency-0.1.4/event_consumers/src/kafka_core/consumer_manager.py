import itertools
import json
import os
import threading
import time
import traceback
import uuid
from typing import Dict, List

import ray
from kafka import KafkaConsumer
from ray.actor import ActorHandle

from event_consumers.src import WORKER_NUM_CPUS, SASL_USERNAME, SASL_PASSWORD, SECURITY_PROTOCOL, \
    SASL_MECHANISM, \
    RAY_HEAD_ADDRESS, LOCAL_MODE, BOOTSTRAP_SERVERS, BOOTSTRAP_SERVERS_DLQ
from event_consumers.src.exceptions.usi_exceptions import BadInput
from event_consumers.src.kafka_core.kafka_util import get_start_end_offsets
from event_consumers.src.kafka_core.ser_des_util import get_ser_des
from event_consumers.src.kafka_core.sink_task import SinkTask
from event_consumers.src.logging import logging_util
from event_consumers.src.utility.common_util import singleton, CLIENT_ID
from event_consumers.src.utility.config_manager import ConfigManager

logger = logging_util.get_logger(__name__)

TWO_MINUTES = 2
MAX_RESTARTS_REMOTE_WORKER = 10
TEN_SECONDS = 10

if LOCAL_MODE == 'Y':
    ray.init()
else:
    ray.init(address=RAY_HEAD_ADDRESS)

logger.warn('''This cluster consists of
    {} nodes in total
    {} CPU resources in total
'''.format(len(ray.nodes()), ray.cluster_resources()['CPU']))


@singleton
class ConsumerWorkerManager:

    def __init__(self):
        self.consumer_worker_container: Dict[str, List[ActorHandle]] = {}
        self.seek_consumer_worker_container: Dict[str, SeekConsumerWorker] = {}
        self.config_manager = ConfigManager()
        self.worker_configs = self.config_manager.get_worker_config()
        self.env_vars: dict = {'BOOTSTRAP_SERVERS': BOOTSTRAP_SERVERS,
                               'NEW_RELIC_APP_NAME': os.environ.get("NEW_RELIC_APP_NAME"),
                               'NEW_RELIC_LICENSE_KEY': os.environ.get("NEW_RELIC_LICENSE_KEY"),
                               'NEW_RELIC_APP_GUID': os.environ.get("NEW_RELIC_APP_GUID"),
                               'BOOTSTRAP_SERVERS_DLQ': BOOTSTRAP_SERVERS_DLQ
                               }
        self.init_container()

    def init_container(self) -> None:
        for worker_config in self.worker_configs:
            self.consumer_worker_container[worker_config.get('consumer_name')] = []

    def stop_all_workers(self):

        for worker_name, worker_actors in self.consumer_worker_container.items():

            for worker_actor in worker_actors:
                # wait on the future to stop the consumers
                ray.get(worker_actor.stop_consumer.remote(), timeout=TEN_SECONDS)

                ray.kill(worker_actor)
            self.consumer_worker_container[worker_name] = []

        logger.info("All consumer workers stopped.")

    def get_all_consumers_health(self) -> dict:
        """
        Function to check the status us each consumers and the assigment details.
        state = GREEN -> all consumers are healthy and running
        state = YELLOW -> Consumers are running and healthy but some of the consumers are not
        assigned any partition.
        state = RED -> All or some consumers belonging to a consumer group are dead
        :return: consumers status
        """
        response: dict = {}
        result: List[Dict] = []
        overall_state = 'GREEN'
        for worker_name, worker_actors in self.consumer_worker_container.items():
            consumer_info: dict = {'consumer_name': worker_name}
            worker_details: list = []
            if worker_actors is None or len(worker_actors) == 0:
                overall_state = 'RED'
            for worker_actor in worker_actors:
                consumer_det: dict = {}
                try:
                    consumer_det: dict = {**ray.get(worker_actor.consumer_info.remote(), timeout=TEN_SECONDS)}

                    if len(consumer_det['assignment']) == 0:
                        consumer_det['state'] = 'NOT ASSIGNED'
                        overall_state = 'YELLOW' if overall_state != 'RED' else 'RED'
                    else:
                        consumer_det['state'] = 'RUNNING'
                except BaseException as e:
                    consumer_det['status'] = 'DEAD'
                    overall_state = 'RED'
                    consumer_det['error_description'] = f'{e}'
                    logger.error(f"Dead consumer found: {e}")
                    logger.error(''.join(traceback.format_exception(None, e, e.__traceback__)))
                worker_details.append(consumer_det)

            consumer_info['workers'] = worker_details

            result.append(consumer_info)
        overall_state = 'GREEN' if overall_state == 'GREEN' else overall_state
        response['details'] = result
        response['state'] = overall_state
        return response

    def get_consumer_health(self, worker_name: str) -> dict:
        workers: List[ActorHandle] = self.consumer_worker_container.get(worker_name)
        overall_state = 'GREEN'
        response: dict = {}
        try:
            consumer_details: list = []
            for worker_actor in workers:
                assignment_info: dict = ray.get(worker_actor.consumer_info.remote(), timeout=TEN_SECONDS)
                consumer_det: dict = {**assignment_info}

                if len(consumer_det['assignment']) == 0:
                    consumer_det['state'] = 'NOT ASSIGNED'
                    overall_state = 'YELLOW' if overall_state != 'RED' else 'RED'
                else:
                    consumer_det['state'] = 'RUNNING'

                consumer_details.append(consumer_det)

            response['details'] = consumer_details
        except BaseException as e:
            overall_state = 'RED'
            response['error_description'] = f'{e}'
            logger.error(f"Dead consumer found: {e}")
            logger.error(''.join(traceback.format_exception(None, e, e.__traceback__)))
        response['state'] = 'GREEN' if overall_state == 'GREEN' else overall_state
        return response

    def _is_actor_alive(self, actor_name) -> bool:
        try:
            ray.get_actor(actor_name)
            return True
        except Exception as e:
            logger.error(e)
            return False

    def start_all_workers(self):
        start_time = time.monotonic()
        started_flag = False
        threads: List = []
        for worker_config in self.worker_configs:
            name = worker_config.get('consumer_name')
            # start consumer only if the consumer workers are not running
            if len(self.consumer_worker_container.get(name)) == 0:
                started_flag = True
                thread = threading.Thread(target=self.start_worker, args=(name,))
                thread.start()
                threads.append(thread)
        if not started_flag:
            raise BadInput(f'All Consumers already running')
        for thread in threads:
            thread.join()
        logger.info("All consumer workers started.")
        logger.info(
            f'time taken to start all consumers: {(time.monotonic() - start_time)} seconds')

    def start_worker(self, name: str) -> str:
        if name not in self.consumer_worker_container:
            raise BadInput(f'Failed to start. Worker {name} not found.')

        if name in self.consumer_worker_container and len(self.consumer_worker_container.get(
                name)) > 0:
            raise BadInput('Consumer already running.')

        worker_config: dict = self.config_manager.get_worker_config_by_name(name)
        num_workers = worker_config.get('number_of_workers', 1)
        worker_config['env_vars'] = self.env_vars
        i = 1
        for _ in itertools.repeat(None, num_workers):
            w_name = name + '-' + str(i)
            worker_actor = ConsumerWorker.options(name=w_name, max_concurrency=3).remote(
                worker_config, w_name)
            # wait for 10 seconds to start consumer
            time.sleep(10)
            if not self._is_actor_alive(w_name):
                return "Failed to Start"
            i = i + 1
            self.consumer_worker_container[name].append(worker_actor)
            try:
                worker_actor.run.remote()
            except BaseException as e:
                logger.error(f'Failed to run worker: {e}')
                logger.error(''.join(traceback.format_exception(None, e, e.__traceback__)))
        logger.info(f"{num_workers} workers of worker group {name} started.")
        return "Successfully started worker!"

    def stop_worker(self, name: str) -> None:
        if name not in self.consumer_worker_container:
            raise BadInput(f'Failed to stop. Worker {name} not found.')

        worker_actors = self.consumer_worker_container[name]

        if len(worker_actors) == 0:
            raise BadInput(f'Worker not running.')

        for worker_actor in worker_actors:
            # wait on the future before killing actors, so that the consumers are terminated
            # gracefully
            ray.get(worker_actor.stop_consumer.remote(), timeout=TEN_SECONDS)

            ray.kill(worker_actor)
        self.consumer_worker_container[name] = []
        logger.info(f"{name} consumer worker stopped.")

    def start_worker_with_timestamp(self, name: str, start_timestamp: int, end_timestamp: int,
                                    stop_regular=False) -> None:
        """
        Performs below steps:
        1. This function will first stop the current running consumer(If stop_regular=true)
        2. Create new consumer with new consumer group
        3. Start seeking all the offset from the start_timestamp till end/current timestamp.
        3. Stops the temporary consumer that was seeking old data.
        4. Start the regular consumer.
        Warning: It is possible that the consumers may read the same data twice. So,
        it is important that the writes are idempotent
        :param name: consumer worker name
        :param start_timestamp: start time in epoch time millis - start consuming data from this
        timestamp
        :param end_timestamp end consuming data from this timestamp, if None passed,
        current timestamp will be used.
        :param stop_regular: if True stops the consumer worker passed in the argument.
        :return: None
        """

        if name in self.seek_consumer_worker_container:
            raise BadInput(f'One seek task for the consumer {name}, is already running.')

        try:
            self.seek_consumer_worker_container[name] = None
            worker_name = name + '-' + str(uuid.uuid4())

            if stop_regular:
                self.stop_worker(name)

            if not end_timestamp:
                end_timestamp = int(time.time() * 1000)

            worker = SeekConsumerWorker(self.config_manager.get_worker_config_by_name(name),
                                        start_timestamp, end_timestamp,
                                        seek_consumer_name=worker_name)

            self.seek_consumer_worker_container[name] = worker
            worker.start()
            worker.join()
        except Exception as e:
            logger.error(f'Failed to consume data from previous timestamp: {e}')
            raise e
        finally:
            if stop_regular:
                self.start_worker(name)

            self.seek_consumer_worker_container.pop(name)


class SeekConsumerWorker(threading.Thread):

    def __init__(self, config: dict, start_timestamp: int, end_timestamp, seek_consumer_name: str):
        threading.Thread.__init__(self)
        self.consumer_name = seek_consumer_name
        self.start_timestamp = start_timestamp
        self.end_timestamp = end_timestamp
        self.stop_event = threading.Event()
        self.config = config
        self.auto_offset_reset = 'earliest'
        self.consumer_timeout_ms = 1000
        self.processed_count = 0
        self.sink_task: SinkTask = SinkTask(config)
        self.consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                      client_id=CLIENT_ID,
                                      group_id=self.consumer_name,
                                      key_deserializer=get_ser_des(self.config.get(
                                          'key_deserializer', 'STRING_DES')),
                                      value_deserializer=get_ser_des(self.config.get(
                                          'value_deserializer', 'JSON_DES')),
                                      auto_offset_reset=self.auto_offset_reset,
                                      enable_auto_commit=self.config.get('enable_auto_commit',
                                                                         True),
                                      max_poll_records=self.config.get('max_poll_records', 50),
                                      max_poll_interval_ms=self.config.get('max_poll_interval_ms',
                                                                           600000),
                                      security_protocol=SECURITY_PROTOCOL,
                                      sasl_mechanism=SASL_MECHANISM,
                                      consumer_timeout_ms=1000)
        self.consumer.subscribe([self.config.get('topic_name')])

    def is_all_partitions_read(self, tp_flag: dict):
        for tp, flag in tp_flag.items():
            if not flag:
                return False
        return True

    def run(self) -> None:
        total_processed = 0

        # do a dummy poll, so kafka can assign partitions to this consumer
        self.consumer.poll()

        # get current assigned partitions
        # warning: create only one consumer, as consumer rebalancing can disrupt partition
        # assignment
        topic_partitions: set = self.consumer.assignment()

        start_offsets, end_offsets = get_start_end_offsets(
            start_timestamp=self.start_timestamp,
            end_timestamp=self.end_timestamp,
            topic_partitions=topic_partitions,
            consumer=self.consumer)

        for tp in topic_partitions:
            self.consumer.seek(tp, start_offsets.get(tp).offset)

        tp_break_flag: dict = {}
        for tp in end_offsets.keys():
            tp_break_flag[tp] = False

        while True:
            try:
                tp_records_dict = self.consumer.poll(timeout_ms=self.consumer_timeout_ms)

                if tp_records_dict is None or len(tp_records_dict.items()) == 0:
                    continue

                for topic_partition, consumer_records in tp_records_dict.items():
                    consumer_records_buffer = []
                    for consumer_record in consumer_records:
                        if consumer_record.offset >= end_offsets[topic_partition].offset:
                            tp_break_flag[topic_partition] = True
                            break
                        consumer_records_buffer.append(consumer_record)
                        total_processed += 1
                    self.sink_task.process(consumer_records_buffer)

                self.consumer.commit()

                if self.is_all_partitions_read(tp_break_flag):
                    self.consumer.close()
                    logger.info(
                        f'stopping seek consumer {self.consumer_name}, '
                        f'total records processed: {total_processed}')
                    break
            except BaseException as e:
                logger.error(e)
                raise e


@ray.remote(max_restarts=MAX_RESTARTS_REMOTE_WORKER, max_task_retries=MAX_RESTARTS_REMOTE_WORKER,
            num_cpus=WORKER_NUM_CPUS)
class ConsumerWorker:
    def __init__(self, config: dict, worker_name: str):
        # creating a separate logger for individual worker. As they only need to print in stdout
        # or stderr
        self._set_env_variables(config)
        self.logger = logging_util.get_logger(__name__)
        self.consumer_name = config.get('consumer_name')
        self.worker_name = worker_name
        self.config = config
        self.stop_worker = False
        self.auto_offset_reset = 'earliest'
        self.poll_timeout_ms = 2000
        self.sink_task: SinkTask = SinkTask(config)
        self.is_closed = False
        # set to double of poll_timeout_ms because - in the next iteration of poll, thread will
        # attempt to stop kafka consumer
        self.consumer_stop_delay_seconds = 2 * self.poll_timeout_ms / 1000
        self.consumer = KafkaConsumer(bootstrap_servers=BOOTSTRAP_SERVERS,
                                      client_id=CLIENT_ID,
                                      group_id=self.consumer_name,
                                      key_deserializer=get_ser_des(self.config.get(
                                          'key_deserializer', 'STRING_DES')),
                                      value_deserializer=get_ser_des(self.config.get(
                                          'value_deserializer', 'JSON_DES')),
                                      auto_offset_reset=self.auto_offset_reset,
                                      enable_auto_commit=self.config.get('enable_auto_commit',
                                                                         True),
                                      max_poll_records=self.config.get('max_poll_records', 50),
                                      max_poll_interval_ms=self.config.get('max_poll_interval_ms',
                                                                           600000),
                                      security_protocol=SECURITY_PROTOCOL,
                                      sasl_mechanism=SASL_MECHANISM,
                                      sasl_plain_username=SASL_USERNAME,
                                      sasl_plain_password=SASL_PASSWORD)
        self.consumer.subscribe([self.config.get('topic_name')])
        self.logger.info(f'Started consumer worker {self.worker_name}')

    def _set_env_variables(self, config: dict):
        env_vars: dict = config.get("env_vars")

        for key, value in env_vars.items():
            os.environ[key] = value

    def stop_consumer(self) -> None:
        self.logger.info(f'Stopping consumer worker {self.worker_name}')
        self.stop_worker = True

        # give time for the consumer to stop gracefully
        time.sleep(self.consumer_stop_delay_seconds)
        self.logger.info(f'Stopped consumer worker {self.worker_name}')

    def closed(self):
        return self.is_closed

    def consumer_info(self) -> dict:
        consumer_info: dict = {}
        metrics = self.consumer.metrics(raw=False)
        topic_partitions: set = self.consumer.assignment()

        consumer_info['assignment'] = list(topic_partitions)
        consumer_info['name'] = self.worker_name
        consumer_info['metrics'] = json.dumps(metrics)
        return consumer_info

    def run(self) -> None:

        while not self.stop_worker:
            try:
                tp_records_dict = self.consumer.poll(timeout_ms=self.poll_timeout_ms)

                if tp_records_dict is None or len(tp_records_dict.items()) == 0:
                    continue

                for topic_partition, consumer_records in tp_records_dict.items():
                    self.sink_task.process(consumer_records)

                self.consumer.commit()
                self.logger.warn(f"{self.consumer_name}.{self.worker_name}: total records "
                                 f"processed:"
                                 f" {len(tp_records_dict)}")

                if self.stop_worker:
                    self.consumer.close()
                    self.is_closed = True
                    break
            except BaseException as e:
                self.logger.error('Error while running consumer worker!')
                self.logger.error(e)
