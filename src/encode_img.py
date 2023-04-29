# built-in imports
from os.path import abspath, join
from base64 import urlsafe_b64encode
# pip installed imports
from requests import get
from src.rips.utils import gpg, hdir


img_fdir = abspath('images')


async def img_url(url):
    img = get(url).content
    return urlsafe_b64encode(img).hex()


def img_file(filename):
    img = f'{img_fdir}/{filename}'
    with open(img, 'rb') as file:
        return urlsafe_b64encode(file.read()).hex()


def encrypt_img(
    filename: str, fingerprint: list[str] | str, pword:str
):
    img = f'{img_fdir}/{filename}'
    return gpg.encrypt_file(img, fingerprint, passphrase=pword, symmetric=True) 