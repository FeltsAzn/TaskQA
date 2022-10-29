from signature_script.ecdsa_digital_signature import check_signature
from tests.testcase.create_testcase import create_test_keys, create_test_signature
import pytest


create_test_keys()
create_test_signature()


test_data = [("testcase/test_secret.txt",
              "testcase/test_secret.sign",
              "testcase/test_public.pem", True),

             ("testcase/test_secret.txt",
              "testcase/false_test_secret.sign",
              "testcase/test_public.pem", False),

             ("testcase/test_secret.txt",
              "testcase/test_secret.sign",
              "testcase/false_test_public.pem", False)]

test_data_errors = [
             ("testcase/test_secret_not_found.txt",
              "testcase/test_secret.sign",
              "testcase/test_public.pem",
              FileNotFoundError),

             ("testcase/test_secret_not_found.txt",
              "testcase/test_secret_not_found.sign",
              "testcase/test_public.pem",
              FileNotFoundError),

             ("testcase/test_secret.txt",
              "testcase/test_secret.sign",
              "testcase/test_public_not_found.pem",
              FileNotFoundError)
             ]


@pytest.mark.parametrize("filename, signature, key, value", test_data)
def test_check_signature(filename: str, signature: str, key: str, value: bool):
    """Test for signature script checker"""
    assert check_signature(filename=filename, signature=signature, key=key) is value


@pytest.mark.parametrize("filename, signature, key, excepted_ex", test_data_errors)
def test_check_signature_with_error(filename: str, signature: str, key: str, excepted_ex):
    """Test for signature script checker with errors"""
    with pytest.raises(excepted_ex):
        check_signature(filename=filename, signature=signature, key=key)
