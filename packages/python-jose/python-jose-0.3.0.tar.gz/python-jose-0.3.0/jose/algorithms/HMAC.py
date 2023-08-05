
import hashlib
import hmac

import six

from jose.algorithms.base import Algorithm
from jose.utils import constant_time_compare


class HMACAlgorithm(Algorithm):
    """
    Performs signing and verification operations using HMAC
    and the specified hash function.
    """
    SHA256 = hashlib.sha256
    SHA384 = hashlib.sha384
    SHA512 = hashlib.sha512

    def __init__(self, hash_alg):
        self.hash_alg = hash_alg

    def process_prepare_key(self, key):
        if not isinstance(key, six.string_types) and not isinstance(key, bytes):
            raise TypeError('Expecting a string- or bytes-formatted key.')

        if isinstance(key, six.text_type):
            key = key.encode('utf-8')

        invalid_strings = [
            b'-----BEGIN PUBLIC KEY-----',
            b'-----BEGIN CERTIFICATE-----',
            b'ssh-rsa'
        ]

        if any([string_value in key for string_value in invalid_strings]):
            raise Exception(
                'The specified key is an asymmetric key or x509 certificate and'
                ' should not be used as an HMAC secret.')

        return key

    def process_sign(self, msg, key):
        return hmac.new(key, msg, self.hash_alg).digest()

    def process_verify(self, msg, key, sig):
        return constant_time_compare(sig, self.sign(msg, key))
