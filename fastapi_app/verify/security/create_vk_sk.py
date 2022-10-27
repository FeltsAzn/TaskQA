from ecdsa import SigningKey
from ecdsa import NIST256p
from hashlib import sha256

sec_key = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
pub_key = sec_key.verifying_key
with open("private.pem", "wb") as f:
    f.write(sec_key.to_pem())
with open("public.pem", "wb") as f:
    f.write(pub_key.to_pem())