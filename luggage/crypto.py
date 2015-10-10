import base64
import os

import six

import attr

from nacl import utils as nutils, public as npublic

def decryptDict(dct, signingPrivateKey, realPrivateKey, realPublicKey):
    """decrypt all values in a dictionary

    Assumes all values in a dictionary are base64ed encrypted with realPublicKey,
    and signed with signingPrivateKey, and decrypt them with realPrivateKey.
    If realPrivateKey and realPublicKey do not correspond to each other,
    or any value in the dictionary is not signed and encrypted correctly,
    an exception is raised.

    :param dct: encrypted dictionary
    :type dct: dictionary with string values and keys
    :param signingPrivateKey: base64 encoded NaCl private key
    :type signingPrivateKey: string
    :param realPrivateKey: base64 encoded NaCl private key
    :type realPrivateKey: string
    :param realPublicKey: base64 encoded NaCl private key
    :type realPublicKey: string
    :rtype: dictionary with string values and keys
    """
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
    """encrypt and sign a value, and base64-encode the result

    :param value: a secret
    :type value: string
    :param signingPrivateKey: base64 encoded NaCl private key
    :type signingPrivateKey: string
    :param realPublicKey: base64 encoded NaCl private key
    :type realPublicKey: string
    :rtype: string
    """
    signingPrivateKey = npublic.PrivateKey(base64.decodestring(signingPrivateKey))
    realPublicKey = npublic.PublicKey(base64.decodestring(realPublicKey))
    box = npublic.Box(signingPrivateKey, realPublicKey)
    nonce = nutils.random(npublic.Box.NONCE_SIZE)
    encrypted = box.encrypt(value, nonce)
    encoded = base64.encodestring(encrypted)
    oneline = ''.join(encoded.splitlines())
    return oneline


@attr.s
class Secrets(object):
    envVar = attr.ib()
    encSecrets = attr.ib()
    signingKey = attr.ib()
    publicKey = attr.ib()
    _cache = None

    def get(self):
        if self._cache == None:
            self._cache = decryptDict(self.encSecrets, self.signingKey, os.environ[self.envVar], self.publicKey)
        return self._cache
