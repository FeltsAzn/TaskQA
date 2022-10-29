from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
import os


dotenv_path = os.path.join(os.path.dirname(__file__), '../.env_test')  # Finding the path of the .env_test file
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
password = bytes(os.getenv("TEST_PASSWORD_FOR_PRIVATE_KEY"), "utf-8")  # Load test secret password on .env_test


def create_test_keys() -> None:
    """Function for create test public and private key"""
    private_key = ec.generate_private_key(ec.SECP256R1())
    serialized_private = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.BestAvailableEncryption(password)
    )
    with open("testcase/test_private.pem", "wb+") as file:
        file.write(serialized_private)

    public_key = private_key.public_key()
    serialized_public = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open("testcase/test_public.pem", "wb+") as file:
        file.write(serialized_public)


def create_test_signature() -> None:
    """Function for create test digital signature with private key"""
    with open("testcase/test_secret.txt", 'rb') as file:
        data = file.read()

    with open("testcase/test_private.pem", 'rb') as private_key:
        serialized_private = private_key.read()
    loaded_private_key = serialization.load_pem_private_key(serialized_private,
                                                            password=password)

    signature = loaded_private_key.sign(data, ec.ECDSA(hashes.SHA256()))
    with open("testcase/test_secret.sign", 'wb') as file:
        file.write(signature)
