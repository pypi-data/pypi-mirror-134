import os

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


def _install_kafka_python():
    os.system('pip install https://github.com/mattoberle/kafka-python/archive/refs/heads/feature/2232\
                         -AWS_MSK_IAM.zip')


setup(
    name='kafka-connect-dependency',
    version='0.1.4',
    author='Search Dev',
    description='Library to run distributed Kafka Consumers using Ray',
    long_description='This library need to be installed in ray nodes. So, ray head and worker '
                     'nodes can find and pickle/unpickle Kafka Consumer modules.',
    keywords=['ray', 'kafka', 'consumer'],
    long_description_content_type="text/markdown",
    py_modules=['event_consumers.src.exceptions.usi_exceptions',
                'event_consumers.src.kafka_core.consumer_manager',
                'event_consumers.src.kafka_core.kafka_stream_writer',
                'event_consumers.src.kafka_core.kafka_util',
                'event_consumers.src.kafka_core.ser_des_util',
                'event_consumers.src.kafka_core.sink_task',
                'event_consumers.src.model.worker_dto',
                'event_consumers.src.stream_writers.stream_writer',
                'event_consumers.src.stream_writers.console_stream_writer',
                'event_consumers.src.stream_writers.es_stream_writer',
                'event_consumers.src.transformers.transformer',
                'event_consumers.src.transformers.test_transformer',
                'event_consumers.src.transformers.api_transformer',
                'event_consumers.src.transformers.collection_transformer',
                'event_consumers.src.transformers.entity_images_transformer',
                'event_consumers.src.transformers.folder_transformer',
                'event_consumers.src.transformers.fork_transformer',
                'event_consumers.src.transformers.organisations_transformer',
                'event_consumers.src.transformers.public_profile_transformer',
                'event_consumers.src.transformers.request_transformer',
                'event_consumers.src.transformers.response_transformer',
                'event_consumers.src.transformers.users_transformer',
                'event_consumers.src.transformers.workspace_slug_transformer',
                'event_consumers.src.transformers.workspace_transformer',
                'event_consumers.src.utility.common_util',
                'event_consumers.src.utility.config_manager',
                'event_consumers.src.logging.logging_util'],
    python_requires='>=3.7',
    install_requires=[
        'fastapi==0.65.1',
        'uvicorn==0.13.4',
        'cachetools~=4.2.2',
        'starlette~=0.14.2',
        'pydantic~=1.7.4',
        'newrelic~=6.8.0.163',
        'ratelimit==2.2.1',
        'ray==1.8.0',
        'boto3==1.20.18',
        'elasticsearch==7.5.1',
        'requests_aws4auth==1.1.1'
    ]
)

_install_kafka_python()
