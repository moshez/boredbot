import base64

import six

from nacl import utils as nutils, public as npublic

def decryptDict(dct, signingPrivateKey, realPrivateKey, realPublicKey):
    signingPrivateKey = npublic.PrivateKey(base64.decodestring(signingPrivateKey))
    signingPublicKey = signingPrivateKey.public_key
    realPrivateKey = npublic.PrivateKey(base64.decodestring(realPrivateKey))
    realPublicKey = npublic.PublicKey(base64.decodestring(realPublicKey))
    if realPrivateKey.public_key.encode() != realPublicKey.encode():
        raise ValueError('private key and public key do not match', realPrivateKey.public_key, realPublicKey)
    box = npublic.Box(realPrivateKey, signingPublicKey)
    ret = {}
    for key, value in six.iteritems(dct):
        decodedValue = base64.decodestring(value)
        decryptedValue = box.decrypt(decodedValue)
        ret[key] = decryptedValue
    return ret

def encrypt(value, signingPrivateKey, realPublicKey):
    signingPrivateKey = npublic.PrivateKey(base64.decodestring(signingPrivateKey))
    realPublicKey = npublic.PublicKey(base64.decodestring(realPublicKey))
    box = npublic.Box(signingPrivateKey, realPublicKey)
    nonce = nutils.random(npublic.Box.NONCE_SIZE)
    encrypted = box.encrypt(value, nonce)
    encoded = base64.encodestring(encrypted)
    oneline = ''.join(encoded.splitlines())
    return oneline

BOREDBOT_MAIN_OK = True
def main(args):
    from boredbot import config
    result = encrypt(args[1], config.SIGNING_KEY, config.PUBLIC_KEY)
    print(result)
