from confluent_kafka import Consumer
from config.kafka_config import KafkaConfig


class KafkaConsumer:
    def __init__(self, topic):
        self.topic = topic

    def get_consumer(self):
        consumer_config = {
            'bootstrap.servers': KafkaConfig.bootstrap_server,
            'group.id': 'test',
            'auto.offset.reset': 'earliest'
        }
        consumer = Consumer(consumer_config)
        consumer.subscribe(self.topic)
        return consumer
