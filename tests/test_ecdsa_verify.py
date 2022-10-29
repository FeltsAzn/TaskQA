from signature_script.ecdsa_digital_signature import check_signature
from create_testcase import create_keys, create_signature
import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env_test')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
print(dotenv_path)
password = bytes(os.getenv("TEST_PASSWORD_FOR_PRIVATE_KEY"), "utf-8")


def test_check_signature():
    """Test for signature script checker"""
    create_keys()
    create_signature()
    filename_path = "test_keys/test_secret.txt"
    signature_path = "test_keys/test_secret.sign"
    pub_key_path = "test_keys/public.pem"
    assert check_signature(filename=filename_path, signature=signature_path, key=pub_key_path) is True


def test_check_signature_false():
    """Test for right error on signature script checker"""
    create_keys()
    create_signature()
    filename_path = "test_keys/test_secret.txt"
    signature_path = "test_keys/false_test_secret.sign"
    pub_key_path = "test_keys/public.pem"
    assert check_signature(filename=filename_path, signature=signature_path, key=pub_key_path) is False
