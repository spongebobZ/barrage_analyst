from confluent_kafka import Consumer, Producer
from config.kafka_config import KafkaConfig


class KafkaProducer:
    def __init__(self, topic):
        self.topic = topic
        producer_conf = {
            'bootstrap.servers': KafkaConfig.bootstrap_server
        }
        self.producer = Producer(producer_conf)

    def produce(self, message):
        self.producer.produce(self.topic, message)
