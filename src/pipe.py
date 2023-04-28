from json import loads
from typing import Any
from subprocess import run, PIPE


APP_EXEC = 'H:\\BlockchainDB\\foxd\\Foxdcoin\\daemon\\foxdcoin-cli.exe'
RPC_USER = 'username'
RPC_PASS = 'password'


def rpc_call(method: str, params: list[Any]) -> dict[str, Any] | None:
    try: result = run((
        lambda m, p: [APP_EXEC,
            f'-rpcuser={RPC_USER}',
            f'-rpcpassword={RPC_PASS}',
            m, *p])(method, params),
            stdout = PIPE)
    except: return
    ret = result.stdout.strip().decode('utf-8')
    if len(ret) == 0: return
    else: return loads(ret)