from ecdsa import VerifyingKey, BadSignatureError, NIST256p, ECDH
from hashlib import sha256
import click


def check_signature(filename: str, signature: str, key: str) -> bool:
    """
    Script for checking the digital signature of a file
    :param filename: Original file
    :param signature: Digital signature for this file
    :param key: Public key to decrypt the signature
    """
    vk = VerifyingKey.from_pem(open(key).read(), hashfunc=sha256)
    with open(filename, "rb") as f:
        message = f.read()
    with open(signature, "rb") as f:
        sig = f.read()
    try:
        vk.verify(sig, message, hashfunc=sha256)
        return True
    except BadSignatureError:
        return False


# Heandler for
@click.command()
@click.option('--f', prompt='Filename', help='--f <FILENAME> -- filename of a signed file')
@click.option('--s', prompt='Signature', help="--s <SIGNATURE> -- filename of a file with signature")
@click.option('--k', prompt='Key', help="--k <KEY> -- filename of a public key")
def script(f: str, s: str, k: str) -> None:
    answer = check_signature(f, s, k)
    click.echo("VALID" if answer else "INVALID")


if __name__ == '__main__':
    # start script
    script()


