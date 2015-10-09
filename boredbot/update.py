import json
import time

import requests

def update(headers):
    data = json.dumps(dict(status="I'm bored"))
    requests.post('https://api.parse.com/1/classes/lines', data=data, headers=headers)

def loop(headers):
    while True:
        update(headers)
        time.sleep(10)
