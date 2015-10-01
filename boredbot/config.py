import os

PARSE_APPLICATION_ID = "sYIULJPxHZCryGbqxbNfsXF8PPU4Blf4Ow5b8SFc"

SECRETS = dict(
    PARSE_REST_API_KEY=os.environ["PARSE_REST_API_KEY"],
    STATE_REST_API_KEY=os.environ["STATE_REST_API_KEY"],
)

HEADERS = {
    "X-Parse-Application-Id": PARSE_APPLICATION_ID,
    "X-Parse-REST-API-Key": SECRETS['PARSE_REST_API_KEY'],
    "Content-Type": "application/json",
}
