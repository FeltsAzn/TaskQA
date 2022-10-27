from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from ecdsa.curves import NIST256p
from hashlib import sha256
import click


# vk = VerifyingKey.from_pem(open("pubk.pem").read(), hashfunc=sha256)
# with open("secret.txt", "r") as f:
#     data = bytes(f.read())
# with open("secret.sign", "rb") as f:
#     signature = f.read()
# try:
#     vk.verify(signature, data)
#     print("good signature")
# except BadSignatureError:
#     print("BAD SIGNATURE")

def create_keys():
    sk = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
    vk = sk.verifying_key
    with open("private.pem", "wb") as f:
        f.write(sk.to_pem())
    with open("public.pem", "wb") as f:
        f.write(vk.to_pem())


with open("private.pem") as f:
    sk = SigningKey.from_pem(f.read())
with open("message", "rb") as f:
    message = f.read()
sig = sk.sign(message)
with open("signature", "wb") as f:
    f.write(sig)

vk = VerifyingKey.from_pem(open("public.pem").read())
with open("message", "rb") as f:
    message = f.read()
with open("signature", "rb") as f:
    sig = f.read()
try:
    vk.verify(sig, message)
    print("good signature")
except BadSignatureError:
    print("BAD SIGNATURE")