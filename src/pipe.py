from os import cpu_count
from json import loads
from typing import Any, Iterable
from subprocess import run, PIPE
from concurrent.futures import ThreadPoolExecutor as thrdplex


APP_EXEC = 'H:\\BlockchainDB\\foxd\\Foxdcoin\\daemon\\foxdcoin-cli.exe'
RPC_USER = 'joshie'
RPC_PASS = 'Babybinky12!'


def rpc_call(method: str, *args: Any) -> dict[str, Any] | None:
    try: result = run((
        lambda m, p: [APP_EXEC,
            f'-rpcuser={RPC_USER}',
            f'-rpcpassword={RPC_PASS}',
            m, *p])(method, args),
            stdout = PIPE)
    except: return
    ret = result.stdout.strip().decode('utf-8')
    if len(ret) == 0: return
    else: return loads(ret)


def thread(method: str, *args):
    with thrdplex(cpu_count()) as tpe: return tpe.submit(rpc_call, method, *args)


def multi_thread(methods: Iterable[str], *args: Any):
    with thrdplex(cpu_count()) as tpe: return tpe.map(rpc_call, methods, args)