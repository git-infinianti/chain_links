from __future__ import annotations
from os import listdir
from os.path import abspath
from json import load
from typing import Any
from pathlib import Path


def main() -> None:
    fdir, ftype = r'src\Database\\params', 'json'
    path = Path.absolute(Path(fdir))
    vars = [f.split('.')[0] for f in listdir(path) if ftype in f]
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
main()

if __name__ == '__main__':
    main()