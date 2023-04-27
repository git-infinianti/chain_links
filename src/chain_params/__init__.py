from os import listdir
from os.path import abspath
from json import load
from typing import Any


def init() -> None:
    fdir, ftype = 'src/chain_params', 'json'
    vars = [f.split('.')[0] for f in listdir(abspath(fdir)) if ftype in f]
    for var in vars:
        with open(abspath(f'{fdir}/{var}.{ftype}'), 'r') as f:
            exec(f'{var} = {load(f)}', globals())
commands: dict[str, Any]
evr: dict[str, Any]
burn_evr: dict[str, Any]
foxd: dict[str, Any]
burn_foxd: dict[str, Any]
rvn: dict[str, Any]
burn_rvn: dict[str, Any]
init()