from boredbot_deploy import config
from luggage import crypto

BOREDBOT_MAIN_OK = True
def main(args):
    result = crypto.encrypt(args[1], config.SECRETS.signingKey, config.SECRETS.publicKey)
    print(result)
