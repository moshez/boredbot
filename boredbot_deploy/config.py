## Application configuration
from luggage import crypto

## Public configuration -- these pose no security risk
## if published.
PARSE_APPLICATION_ID = "sYIULJPxHZCryGbqxbNfsXF8PPU4Blf4Ow5b8SFc"
STATE_APPLICATION_ID = "jcMhpH2gLjin9TK3oQH25Nn4kOG1XQHE8K0WmySL"

## Secret configuration -- these API keys would be a problem
## to publish. They are encrypted here with the public key
## defined. Note that the signing key here is a *private*
## key: this means that anyone could put other values
## and get us to trust them. In practice this is not a problem,
## since anyone who manages to gain *write-access* to the
## dictionary can do far worse.
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
