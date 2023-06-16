import json
from time import sleep
from datetime import datetime
import requests

from config.bilibili_config import BiliBiliConfig
from config.kafka_config import KafkaConfig
from util.kafka_producer import KafkaProducer
from util.mysql_client import MysqlClient


class Collector:
    def __init__(self, room_id, interval):
        self.room_id = str(room_id)
        self.interval = interval

    def run(self):
        url = BiliBiliConfig.url + self.room_id

        session = requests.Session()
        producer = KafkaProducer(KafkaConfig.ods_topic + self.room_id)
        ts_watermark = self.init_ts_watermark()

        while True:
            response = session.get(url)
            if response.status_code == 200:
                messages = json.loads(response.content)['data']['room']
                checked = False
                for message in messages:
                    if not checked:
                        ts = datetime.strptime(message['timeline'], "%Y-%m-%d %H:%M:%S")
                        if ts <= ts_watermark:
                            continue
                        checked = True
                    producer.produce(json.dumps(message))
                if checked:
                    ts_watermark = datetime.strptime(messages[-1]['timeline'], "%Y-%m-%d %H:%M:%S")
                sleep(self.interval)

    def init_ts_watermark(self):
        mysql_client = MysqlClient()
        last_ts_watermark = mysql_client.query_last_ts_watermark(self.room_id)
        return datetime.min if last_ts_watermark is None else datetime.strptime(last_ts_watermark, "%Y-%m-%d %H:%M:%S")

