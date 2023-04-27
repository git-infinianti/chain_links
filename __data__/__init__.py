from os import listdir
from os.path import abspath
from json import load
from typing import Any


def init() -> None:
    fdir, ftype = '__data__', 'json'
    vars = [f.split('.')[0] for f in listdir(abspath(fdir)) if ftype in f]
    for var in vars: 
        with open(abspath(f'{fdir}/{var}.{ftype}'), 'r') as f: 
            exec(f'{var} = {load(f)}', globals())
users: dict[str, Any]
credentials: dict[str, Any]
settings: dict[str, Any]
sighash: dict[str, Any]
mnemonic: list[Any]
init()