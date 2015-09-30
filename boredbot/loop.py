import json
import time

import requests

from boredbot import config

HEADERS = {
    "X-Parse-Application-Id": config.PARSE_APPLICATION_ID,
    "X-Parse-REST-API-Key": config.SECRETS['PARSE_REST_API_KEY'],
    "Content-Type": "application/json",
}

def update():
    data = json.dumps(dict(status="I'm bored"))
    requests.post('https://api.parse.com/1/classes/lines', data=data, headers=HEADERS)

## Execute main from the command-line
BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    while True:
        update()
        time.sleep(10)