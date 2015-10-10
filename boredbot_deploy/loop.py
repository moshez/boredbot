## Simple main wrapper that takes the 
## headers from the configuration and passes
## them to the updating robot.
from boredbot import update, parse
from boredbot_deploy import config

## Execute main from the command-line
BOREDBOT_MAIN_OK = True
def main(dummyArgs):
    headers = parse.getHeaders(config.PARSE_APPLICATION_ID, config.SECRETS.get()['PARSE_REST_API_KEY'])
    update.loop(headers)
