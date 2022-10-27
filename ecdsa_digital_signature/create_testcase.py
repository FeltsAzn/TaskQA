from ecdsa import SigningKey, VerifyingKey, BadSignatureError
from ecdsa.curves import NIST256p
from hashlib import sha256


def create_keys():
    sk = SigningKey.generate(curve=NIST256p, hashfunc=sha256)
    vk = sk.verifying_key
    with open("private.pem", "wb") as f:
        f.write(sk.to_pem())
    with open("public.pem", "wb") as f:
        f.write(vk.to_pem())


def create_signature():
    with open("private.pem") as f:
        sk = SigningKey.from_pem(f.read())
    with open("secret.txt", "rb") as f:
        message = f.read()
    sig = sk.sign(message)
    with open("secret.sign", "wb") as f:
        f.write(sig)


def check_signature():
    vk = VerifyingKey.from_pem(open("public.pem").read())
    with open("secret.txt", "rb") as f:
        message = f.read()
    with open("secret.sign", "rb") as f:
        sig = f.read()
    try:
        vk.verify(sig, message)
        print("good signature")
    except BadSignatureError:
        print("BAD SIGNATURE")


if __name__ == '__main__':
    create_keys()
    create_signature()
    check_signature()