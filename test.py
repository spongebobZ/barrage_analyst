import json
from config.bilibili_config import BiliBiliConfig
from time import sleep

import requests

room_id = 21693526
url = BiliBiliConfig.url + str(room_id)
interval = 1

session = requests.Session()

while True:
    response = session.get(url)
    print(json.loads(response.content))
    sleep(interval)
