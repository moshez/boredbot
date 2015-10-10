## Help developers do the right thing --
## when getting a new API key, they can encrypt
## it and add it to the configuration.
## This automatically base64-s the output
## for easy copy-and-paste into the code.
from luggage import crypto

from boredbot_deploy import config

BOREDBOT_MAIN_OK = True
def main(args):
    result = crypto.encrypt(args[1], config.SECRETS.signingKey, config.SECRETS.publicKey)
    print(result)
