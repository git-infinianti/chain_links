# built-in imports
from json import dumps
from pathlib import Path
from hashlib import sha256
from binascii import crc32
from logging import Logger
from typing import Any, TypeAlias
# pip installed imports
from gnupg import GPG

# Types
PGPBlock: TypeAlias = str
Fingerprint: TypeAlias = str
HashSha256: TypeAlias = str

# Globals
hdir = Path.home()
encoding = 'ascii'
cipher = 'ECDSA'
curve = 'secp256k1'

# Encoder
gpg = GPG()
gpg.encoding = encoding


def sign(metadata: dict[str, Any]) -> HashSha256: return sha256(bytes(dumps(metadata), 'ascii')).hexdigest()
def p2pkh_chksum(p2pkh): return hex(crc32(bytes(p2pkh, encoding)))
def get_pgp_block(fp: str): return gpg.export_keys(fp, expect_passphrase=False)


def gen_key(sym: str, p2pkh:str, pw: str) -> Fingerprint: input_data = gpg.gen_key_input(
        name_real = p2pkh,
        name_email = f'{p2pkh}@{str(sym).lower()}.coin',
        passphrase = pw,
        key_type = cipher,
        key_curve = curve,
    ); gpg.add_subkey(fp := str(gpg.gen_key(input_data)), pw, curve); return fp


def encrypt_files(
    fpath: str, recipients: PGPBlock | list[PGPBlock], signer_fingerprint: Fingerprint, pw:str, cipher_algorithm
) -> PGPBlock: return gpg.encrypt_file(fpath, recipients, signer_fingerprint, passphrase=pw, symmetric=cipher_algorithm) 