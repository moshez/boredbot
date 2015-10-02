import json
import time

import requests

from boredbot import config

def update():
    data = json.dumps(dict(status="I'm bored"))
    requests.post('https://api.parse.com/1/classes/lines', data=data, headers=config.getHeaders())

## Execute main from the command-line
BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    while True:
        update()
        time.sleep(10)
