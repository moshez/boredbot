import os

from boredbot import crypto

PARSE_APPLICATION_ID = "sYIULJPxHZCryGbqxbNfsXF8PPU4Blf4Ow5b8SFc"
STATE_APPLICATION_ID = "jcMhpH2gLjin9TK3oQH25Nn4kOG1XQHE8K0WmySL"

SIGNING_KEY = "p14AmTX3SAR7wdN3+6HHWXdTiYhkMG9XzsztBoxnhr4="
PUBLIC_KEY = "1Wy7uKOcaa5p/5BiMJ82M7v+1c3+SB0DesMTWIj5AxU="

_SECRETS = dict(
    PARSE_REST_API_KEY="a9uodFprEyR4K/xKP7I4lCmafObPac/67+pHGy2So3TzVTZJuLU2oZqt+kBr3pGFvyb/ZMWANaMPkFadXmkv/RlYWeQBO9gBo+/ziTNNjy0=",
    STATE_REST_API_KEY="wSRKdcA5JbXjXV5/4BIIoiVxrwgbp0DHAiT1O1Qrqa9ACRuytA2yOmo6Je05p/5pRHiKi2VQ/BMXxCRBWrBTOqE+TqG/EWkaRj8vSxQYj4I=",
)

_DECRYPTED_SECRETS = None
def getSecrets():
    global _DECRYPTED_SECRETS
    if _DECRYPTED_SECRETS == None:
        _DECRYPTED_SECRETS = crypto.decryptDict(_SECRETS, SIGNING_KEY, os.environ['SECRET_KEY'], PUBLIC_KEY)
    print _DECRYPTED_SECRETS
    return _DECRYPTED_SECRETS

def getHeaders():
    return {
        "X-Parse-Application-Id": PARSE_APPLICATION_ID,
        "X-Parse-REST-API-Key": getSecrets()['PARSE_REST_API_KEY'],
        "Content-Type": "application/json",
    }

def getStateHeaders():
    return {
        "X-Parse-Application-Id": STATE_APPLICATION_ID,
        "X-Parse-REST-API-Key": getSecrets()['STATE_REST_API_KEY'],
    }
