from signature_script.ecdsa_digital_signature import check_signature
from tests.create_testcase import create_test_keys, create_test_signature
import pytest


create_test_keys("testcase_script")
create_test_signature("testcase_script")


test_data = [("testcase_script/test_secret.txt",
              "testcase_script/test_secret.sign",
              "testcase_script/test_public.pem", True),

             ("testcase_script/test_secret.txt",
              "testcase_script/false_test_secret.sign",
              "testcase_script/test_public.pem", False),

             ("testcase_script/test_secret.txt",
              "testcase_script/test_secret.sign",
              "testcase_script/false_test_public.pem", False)]

test_data_errors = [
             ("testcase_script/test_secret_not_found.txt",
              "testcase_script/test_secret.sign",
              "testcase_script/test_public.pem",
              FileNotFoundError),

             ("testcase_script/test_secret.txt",
              "testcase_script/test_secret_not_found.sign",
              "testcase_script/test_public.pem",
              FileNotFoundError),

             ("testcase_script/test_secret.txt",
              "testcase_script/test_secret.sign",
              "testcase_script/test_public_not_found.pem",
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
