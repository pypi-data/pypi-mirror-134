import base64
import hashlib
from Crypto.Cipher import AES

try:
    import secrets
    HAVE_SECRETS = True
except ImportError:
    from Crypto import Random
    HAVE_SECRETS = False


class AESCipher(object):
    def __init__(self, key="677d3cfc-dd28-4a4e-94d5-7c3b99a24a2a"):
        self.bs = 32
        self.key = hashlib.sha256(key.encode()).digest()

    def encrypt(self, raw):
        raw = self._pad(raw)
        if HAVE_SECRETS:
            iv = secrets.token_bytes(16)
        else:
            iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return base64.urlsafe_b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = base64.urlsafe_b64decode(enc)
        iv = enc[: AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return self._unpad(cipher.decrypt(enc[AES.block_size :])).decode("utf-8")

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    @staticmethod
    def _unpad(s):
        return s[: -ord(s[len(s) - 1 :])]
