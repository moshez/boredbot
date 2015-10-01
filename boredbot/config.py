import os

PARSE_APPLICATION_ID = "sYIULJPxHZCryGbqxbNfsXF8PPU4Blf4Ow5b8SFc"
STATE_APPLICATION_ID = "jcMhpH2gLjin9TK3oQH25Nn4kOG1XQHE8K0WmySL"

SECRETS = dict(
    PARSE_REST_API_KEY=os.environ["PARSE_REST_API_KEY"],
    STATE_REST_API_KEY=os.environ["STATE_REST_API_KEY"],
)

HEADERS = {
    "X-Parse-Application-Id": PARSE_APPLICATION_ID,
    "X-Parse-REST-API-Key": SECRETS['PARSE_REST_API_KEY'],
    "Content-Type": "application/json",
}

STATE_HEADERS = {
    "X-Parse-Application-Id": STATE_APPLICATION_ID,
    "X-Parse-REST-API-Key": SECRETS['STATE_REST_API_KEY'],
}
