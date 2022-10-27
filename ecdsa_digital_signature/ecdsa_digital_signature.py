from ecdsa import VerifyingKey, BadSignatureError
from hashlib import sha256
import click


def check_signature(filename: str, signature: str, key: str) -> str:
    vk = VerifyingKey.from_pem(open(key).read(), hashfunc=sha256)
    with open(filename, "rb") as f:
        message = f.read()
    with open(signature, "rb") as f:
        sig = f.read()
    try:
        vk.verify(sig, message)
        return "VALID"
    except BadSignatureError:
        return "INVALID"


@click.command()
@click.option('--f', prompt='Filename', help='--f <FILENAME> -- filename of a signed file')
@click.option('--s', prompt='Signature', help="--s <SIGNATURE> -- filename of a file with signature")
@click.option('--k', prompt='Key', help="--k <KEY> -- filename of a public key")
def script(f, s, k):
    answer = check_signature(f, s, k)
    click.echo(answer)


if __name__ == '__main__':
    script()