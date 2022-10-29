from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import click


def check_signature(filename: str, signature: str, key: str) -> bool:
    """
    Function for verifying the digital signature of a file using a public key
    :param filename: the name of the source file to search in the task folder
    :param signature: signed file with private key
    :param key: public key to verify correct verification
    """
    try:
        with open(f'{filename}', 'rb') as file:
            message = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File "{filename}" not found. Please check directory')

    try:
        with open(f'{signature}', 'rb') as file:
            sig = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File "{signature}" not found. Please check directory')

    try:
        with open(f'{key}', 'rb') as file:
            serialized_public = file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f'File "{key}" not found. Please check directory')

    loaded_public_key = serialization.load_pem_public_key(serialized_public)

    try:
        loaded_public_key.verify(signature=sig,
                                 data=message,
                                 signature_algorithm=ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


# Heandler for flags
@click.command()
@click.option('--f', prompt='Filename', help='--f <FILENAME> -- filename of a signed file')
@click.option('--s', prompt='Signature', help="--s <SIGNATURE> -- filename of a file with signature")
@click.option('--k', prompt='Key', help="--k <KEY> -- filename of a public key")
def script(f: str, s: str, k: str) -> None:
    try:
        answer = check_signature(f, s, k)
    except Exception as ex:
        click.echo(ex)
    else:
        click.echo("VALID" if answer else "INVALID")


if __name__ == '__main__':
    # start script
    script()
