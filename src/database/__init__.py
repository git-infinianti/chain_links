from __future__ import annotations
from os import listdir
from pathlib import Path
from json import load
from typing import Any


def main() -> None:
    fdir, ftype = r'src\Database', 'json'
    path = Path.absolute(Path(fdir))
    vars = [f.split('.')[0] for f in listdir(path) if ftype in f]
    for var in vars: 
        with open(Path.absolute(Path(f'{fdir}/{var}.{ftype}')), 'r') as f: 
            exec(f'{var} = {load(f)}', globals())
users: dict[str, Any]
credentials: dict[str, Any]
settings: dict[str, Any]
sighash: dict[str, Any]
mnemonic: dict[str, list[str]]
main()

if __name__ == '__main__':
    main()