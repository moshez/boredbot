import os

from luggage import crypto

from boredbot import parse

PARSE_APPLICATION_ID = "sYIULJPxHZCryGbqxbNfsXF8PPU4Blf4Ow5b8SFc"
STATE_APPLICATION_ID = "jcMhpH2gLjin9TK3oQH25Nn4kOG1XQHE8K0WmySL"

SECRETS = crypto.Secrets(
    envVar='SECRET_KEY',
    publicKey="1Wy7uKOcaa5p/5BiMJ82M7v+1c3+SB0DesMTWIj5AxU=",
    signingKey="p14AmTX3SAR7wdN3+6HHWXdTiYhkMG9XzsztBoxnhr4=",
    encSecrets=
        dict(
            PARSE_REST_API_KEY="a9uodFprEyR4K/xKP7I4lCmafObPac/67+pHGy2So3TzVTZJuLU2oZqt+kBr3pGFvyb/ZMWANaMPkFadXmkv/RlYWeQBO9gBo+/ziTNNjy0=",
            STATE_REST_API_KEY="wSRKdcA5JbXjXV5/4BIIoiVxrwgbp0DHAiT1O1Qrqa9ACRuytA2yOmo6Je05p/5pRHiKi2VQ/BMXxCRBWrBTOqE+TqG/EWkaRj8vSxQYj4I=",
        ),
)
