from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.exceptions import InvalidSignature
import click


def check_signature(filename: str, signature: str, key: str) -> bool:
    with open(filename, 'rb') as file:
        message = file.read()

    with open(signature, 'rb') as file:
        sig = file.read()

    with open(key, 'rb') as file:
        serialized_public = file.read()
    loaded_public_key = serialization.load_pem_public_key(serialized_public)
    try:
        loaded_public_key.verify(signature=sig,
                                 data=message,
                                 signature_algorithm=ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False


@click.command()
@click.option('--f', prompt='Filename', help='--f <FILENAME> -- filename of a signed file')
@click.option('--s', prompt='Signature', help="--s <SIGNATURE> -- filename of a file with signature")
@click.option('--k', prompt='Key', help="--k <KEY> -- filename of a public key")
def script(f, s, k):
    answer = check_signature(f, s, k)
    click.echo("VALID" if answer else "INVALID")


if __name__ == '__main__':
    # start check script
    script()
