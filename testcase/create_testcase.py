from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature


def create_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    serialized_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(b"key")
    )
    with open("private.pem", "wb+") as file:
        file.write(serialized_private)

    serialized_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("public.pem", "wb+") as file:
        file.write(serialized_public)
    return private_key


def create_signature(private_key):
    with open("secret.txt", 'rb') as file:
        data = file.read()

    signature = private_key.sign(data, ec.ECDSA(hashes.SHA256()))

    with open("secret.sign", 'wb') as file:
        file.write(signature)


def check_signature():
    with open("secret.txt", 'rb') as file:
        message = file.read()

    with open("secret.sign", 'rb') as file:
        signature = file.read()

    with open("public.pem", 'rb') as file:
        serialized_public = file.read()
    loaded_public_key = serialization.load_pem_public_key(serialized_public)
    try:
        loaded_public_key.verify(signature=signature,
                                 data=message,
                                 signature_algorithm=ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


create_keys()
create_signature(private_key)
check_signature()