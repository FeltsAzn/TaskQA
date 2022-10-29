from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '.env_test')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
password = bytes(os.getenv("TEST_PASSWORD_FOR_PRIVATE_KEY"), "utf-8")


def create_keys():
    private_key = ec.generate_private_key(ec.SECP256R1())
    public_key = private_key.public_key()

    serialized_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    )
    with open("test_keys/private.pem", "wb+") as file:
        file.write(serialized_private)

    serialized_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("test_keys/public.pem", "wb+") as file:
        file.write(serialized_public)
    return private_key


def create_signature():
    with open("test_keys/test_secret.txt", 'rb') as file:
        data = file.read()
    with open("test_keys/private.pem", 'rb') as private_key:
        serialized_private = private_key.read()
    loaded_private_key = serialization.load_pem_private_key(serialized_private,
                                                            password=password)

    signature = loaded_private_key.sign(data, ec.ECDSA(hashes.SHA256()))

    with open("test_keys/test_secret.sign", 'wb') as file:
        file.write(signature)
