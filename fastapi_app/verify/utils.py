from ecdsa import SigningKey, VerifyingKey, BadSignatureError
import os


def asymmetric_encryption(file, filename: str) -> str:
    """
    Function for signing a file
    :param file: File data submitted by the user
    :type file: SpooledTemporaryFile
    :param filename: Filename of submitted file by user
    """
    print(type(file))
    with open("verify/security/private.pem") as f:
        sk = SigningKey.from_pem(f.read())
    with open(f'temporary_files/{filename}.sign', "wb") as uploaded_file:
        message = file.read()

        sig = sk.sign(message)
        uploaded_file.write(sig)
    file.close()
    path = os.path.abspath(f'temporary_files') + f'/{filename}.sign'
    return path


async def signature_validator(file, signature) -> bool:
    """
    Function for check digital signature
    :param file: File data submitted by the user
    :type file: SpooledTemporaryFile
    :param signature: Digital signature submitted by user
    :type signature: SpooledTemporaryFile
    """
    vk = VerifyingKey.from_pem(open("verify/security/public.pem").read())
    message = await file.read()
    sig = await signature.read()
    try:
        vk.verify(sig, message)
        return True
    except BadSignatureError:
        return False