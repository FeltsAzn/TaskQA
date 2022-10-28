from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import os
import dotenv

dotenv.load_dotenv()
password_from_env = os.getenv("PASSWORD_FOR_PRIVATE_KEY")
password = bytes(password_from_env, "utf-8")


def asymmetric_encryption(file, filename: str) -> str:
    with open("verify/security/private.pem", 'rb') as private_key:
        serialized_private = private_key.read()
    loaded_private_key = serialization.load_pem_private_key(serialized_private,
                                                            password=password)
    with open(f'temporary_files/{filename}.sign', "wb") as uploaded_file:
        message = file.read()

        signature = loaded_private_key.sign(message, ec.ECDSA(hashes.SHA256()))
        uploaded_file.write(signature)
    file.close()
    path = os.path.abspath(f'temporary_files') + f'/{filename}.sign'
    return path


async def signature_validator(file, signature,) -> bool:
    """
    Function for check digital signature
    :param file: File data submitted by the user
    :type file: SpooledTemporaryFile
    :param signature: Digital signature submitted by user
    :type signature: SpooledTemporaryFile
    """
    message = await file.read()
    sig = await signature.read()

    with open(f"verify/security/public.pem", 'rb') as file:
        serialized_public = file.read()
    loaded_public_key = serialization.load_pem_public_key(serialized_public)
    try:
        loaded_public_key.verify(signature=sig,
                                 data=message,
                                 signature_algorithm=ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False
