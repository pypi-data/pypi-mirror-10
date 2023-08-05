import binascii
import hashlib

from collections import OrderedDict

from django.apps import apps

from ..constants import (KEY_FILENAMES, HASH_PREFIX, CIPHER_PREFIX, ENCODING, HASH_ALGORITHM, HASH_ROUNDS)
from ..exceptions import CipherError, EncryptionError, MalformedCiphertextError, EncryptionKeyError

from .cryptor import Cryptor
from .keys import KEYS


class FieldCryptor(object):
    """ Base class for django field classes with encryption.

    ciphertext = hash_prefix + hashed_value + cipher_prefix + secret

    The plaintext is hashed and stored by the user's model field. The plaintext is
    also encrypted and stored in the cipher model along with the hash. The user's
    model field object looks up the secret in the cipher model using the hash.
    The secret is decrypted and returned to the user's model field object.

    """
    def __init__(self, algorithm, mode):
        self._cipher_model = None
        self.cipher_buffer = OrderedDict()
        self.algorithm = algorithm
        self.mode = mode
        self.cryptor = Cryptor()
        self.hash_size = len(self.hash('Foo'))

    @property
    def cipher_model(self):
        """Returns the cipher model and avoids issues with model loading and field classes."""
        if not self._cipher_model:
            self._cipher_model = apps.get_model('django_crypto_fields', 'Crypt')
        return self._cipher_model

    def hash(self, plaintext):
        """Returns a hexified hash of a plaintext value.

        The hashed value is used as a signature of the "secret"."""
        try:
            plaintext = plaintext.encode(ENCODING)
        except AttributeError:
            pass
        try:
            salt = KEYS['salt'][self.mode]['private']
        except AttributeError:
            raise EncryptionKeyError('Invalid mode for salt key. Got {}'.format(self.mode))
        dk = hashlib.pbkdf2_hmac(HASH_ALGORITHM, plaintext, salt, HASH_ROUNDS)
        return binascii.hexlify(dk)

    def encrypt(self, value, update=None):
        """ Returns ciphertext as byte data using either an RSA or AES cipher.

        * 'value' is either plaintext or ciphertext
        * 'ciphertext' is a byte value of hash_prefix + hashed_value + cipher_prefix + secret.
          For example: enc1:::234234ed234a24enc2::\x0e\xb9\xae\x13s\x8d\xe7O\xbb\r\x99.
        * 'value' is not re-encrypted if already encrypted and properly formatted 'ciphertext'.
        """
        if value is None:
            return None
        update = True if update is None else update
        if self.is_encrypted(value):
            try:
                value = value.encode(ENCODING)
            except AttributeError:
                pass
        else:
            try:
                if self.algorithm == 'aes':
                    cipher = self.cryptor.aes_encrypt
                elif self.algorithm == 'rsa':
                    cipher = self.cryptor.rsa_encrypt
                else:
                    cipher = None
                ciphertext = (HASH_PREFIX.encode(ENCODING) + self.hash(value) +
                              CIPHER_PREFIX.encode(ENCODING) + cipher(value, self.mode))
                if update:
                    self.update_cipher_model(ciphertext)
            except AttributeError as e:
                raise CipherError(
                    'Cannot determine cipher method. Unknown encryption algorithm. '
                    'Valid options are {0}. Got {1} ({2})'.format(', '.join(KEY_FILENAMES), self.algorithm, e))
        return ciphertext

    def decrypt(self, hash_with_prefix):
        """Returns decrypted secret.

        Secret is retrieved from cipher_model using the hash.

        hash_with_prefix = hash_prefix+hash."""
        plaintext = None
        if hash_with_prefix:
            if self.is_encrypted(hash_with_prefix, has_secret=False):
                hashed_value = self.get_hash(hash_with_prefix)
                secret = self.fetch_secret(hash_with_prefix)
                if secret:
                    if self.algorithm == 'aes':
                        plaintext = self.cryptor.aes_decrypt(secret, self.mode)
                    elif self.algorithm == 'rsa':
                        plaintext = self.cryptor.rsa_decrypt(secret, self.mode)
                    else:
                        raise CipherError(
                            'Cannot determine algorithm for decryption.'
                            ' Valid options are {0}. Got {1}'.format(
                                ', '.join(list(KEY_FILENAMES)), self.algorithm))
                else:
                    hashed_value = self.get_hash(hash_with_prefix)
                    if hashed_value:
                        raise EncryptionError(
                            'Failed to decrypt. Could not find "secret" '
                            ' for hash \'{0}\''.format(hashed_value))
                    else:
                        raise EncryptionError('Failed to decrypt. Malformed ciphertext')
        return plaintext

    def update_cipher_model(self, ciphertext):
        """ Updates cipher model (Crypt) and temporary buffer."""
        if self.verify_ciphertext(ciphertext):
            hashed_value = self.get_hash(ciphertext)
            secret = self.get_secret(ciphertext)
            self.cipher_buffer.update({hashed_value: secret})
            try:
                cipher_model = self.cipher_model.objects.get(hash=hashed_value)
                cipher_model.secret = secret
            except self.cipher_model.DoesNotExist:
                self.cipher_model.objects.create(
                    hash=hashed_value,
                    secret=secret,
                    algorithm=self.algorithm,
                    mode=self.mode)

    def verify_ciphertext(self, ciphertext):
        """Returns ciphertext after verifying format prefix + hash + prefix + secret."""
        try:
            ciphertext.split(HASH_PREFIX.encode(ENCODING))[1]
            ciphertext.split(CIPHER_PREFIX.encode(ENCODING))[1]
        except IndexError:
            ValueError('Malformed ciphertext. Expected prefixes {}, {}'.format(HASH_PREFIX, CIPHER_PREFIX))
        try:
            if ciphertext[:len(HASH_PREFIX)] != HASH_PREFIX.encode(ENCODING):
                raise MalformedCiphertextError(
                    'Malformed ciphertext. Expected hash prefix {}'.format(HASH_PREFIX))
            if (len(ciphertext.split(HASH_PREFIX.encode(ENCODING))[1].split(
                    CIPHER_PREFIX.encode(ENCODING))[0]) != self.hash_size):
                raise MalformedCiphertextError(
                    'Malformed ciphertext. Expected hash size of {}.'.format(self.hash_size))
        except IndexError:
            MalformedCiphertextError('Malformed ciphertext.')
        return ciphertext

    def get_query_value(self, ciphertext):
        """ Returns the prefix + hash as stored in the DB's table column.

        Used by get_prep_value()"""
        return ciphertext.split(CIPHER_PREFIX.encode(ENCODING))[0]

    def get_hash(self, ciphertext):
        """Returns the hashed_value given a ciphertext or None."""
        return ciphertext[len(HASH_PREFIX):][:self.hash_size] or None

    def get_secret(self, ciphertext):
        """ Returns the secret given a ciphertext."""
        if ciphertext is None:
            secret = None
        if self.is_encrypted(ciphertext):
            secret = ciphertext.split(CIPHER_PREFIX.encode(ENCODING))[1]
        return secret

    def fetch_secret(self, hash_with_prefix):
        hashed_value = self.get_hash(hash_with_prefix)
        secret = self.cipher_buffer.get(hashed_value)
        if not secret:
            try:
                cipher_model = self.cipher_model.objects.values('secret').get(hash=hashed_value)
                secret = cipher_model.get('secret')
                self.cipher_buffer.update({hashed_value: secret})
            except self.cipher_model.DoesNotExist:
                raise EncryptionError(
                    'Failed to get secret for given hash. Got {0}'.format(hashed_value))
        return secret

    def is_encrypted(self, value, has_secret=None):
        """Returns True if value is encrypted."""
        has_secret = True if has_secret is None else has_secret
        value = self.verify_value(value, has_secret)
        if value is None:
            return False
        is_encrypted = False
        if (value[:len(HASH_PREFIX)] == HASH_PREFIX.encode(ENCODING) or
                value[:len(CIPHER_PREFIX)] == CIPHER_PREFIX.encode(ENCODING)):
            is_encrypted = True
        return is_encrypted

    def verify_value(self, value, has_secret=None):
        """Encodes the value, validates its format, and returns it or raises an exception.

        A value is either a value that can be encrypted or one that already is encrypted.

        * A value cannot just be equal to HASH_PREFIX or CIPHER_PREFIX;
        * A value prefixed with HASH_PREFIX must be followed by a valid hash (by length);
        * A value prefixed with HASH_PREFIX + hashed_value + CIPHER_PREFIX must be followed by some text;
        * A value prefix by CIPHER_PREFIX must be followed by some text;
        """
        has_secret = True if has_secret is None else has_secret
        if value is None:
            return value
        try:
            value = value.encode(ENCODING)
        except AttributeError:
            pass
        if value in [HASH_PREFIX.encode(ENCODING), CIPHER_PREFIX.encode(ENCODING)]:
            raise MalformedCiphertextError('Expected a value, got just the encryption prefix.')
        self.verify_hash(value)
        self.verify_secret(value, has_secret)
        return value

    def verify_hash(self, ciphertext):
        """Verifies hash segment of ciphertext and raises an exception if not OK."""
        if (ciphertext[:len(HASH_PREFIX)] == HASH_PREFIX.encode(ENCODING) and
                len(ciphertext[len(HASH_PREFIX):].split(CIPHER_PREFIX.encode(ENCODING))[0]) != self.hash_size):
            raise MalformedCiphertextError(
                'Expected hash prefix to be followed by a hash. Got something else or nothing')

    def verify_secret(self, ciphertext, has_secret):
        """Verifies secret segment of ciphertext and raises an exception if not OK."""
        if ciphertext[:len(HASH_PREFIX)] == HASH_PREFIX.encode(ENCODING) and has_secret:
            if CIPHER_PREFIX.encode(ENCODING) not in ciphertext:
                raise MalformedCiphertextError('Expected cipher prefix. Got nothing')
            try:
                secret = ciphertext.split(CIPHER_PREFIX.encode(ENCODING))[1]
                if len(secret) == 0:
                    raise MalformedCiphertextError('Expected cipher prefix to be followed by secret. Got nothing')
            except IndexError:
                raise MalformedCiphertextError('Expected cipher prefix to be followed by secret. Got nothing')
        if (ciphertext[-1 * len(CIPHER_PREFIX):] == CIPHER_PREFIX.encode(ENCODING) and
                len(ciphertext.split(CIPHER_PREFIX.encode(ENCODING))[1]) == 0):
            raise MalformedCiphertextError('Expected cipher prefix to be followed by a secret. Got nothing')

    def mask(self, value, mask=None):
        """ Returns 'mask' if value is encrypted."""
        mask = mask or '<encrypted>'
        if self.is_encrypted(value):
            return mask
        else:
            return value
