from os import getenv, cpu_count
from json import loads
from typing import Any
from subprocess import run, PIPE
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from dotenv import load_dotenv


def rpc_call(method: str, *args: Any) -> dict[str, Any] | None:
    if load_dotenv():
        APPEXEC = str(getenv('APPEXEC'))
        RPCUSER = getenv('RPCUSER')
        RPCPASS = getenv('RPCPASS')
    try: result = run((
        lambda m: [APPEXEC,
            f'-rpcuser={RPCUSER}',
            f'-rpcpassword={RPCPASS}',
            m, *args])(method),
            stdout = PIPE)
    except: return
    ret = result.stdout.strip().decode('utf-8')
    if len(ret) == 0: return
    else: return loads(ret)

class RPCExec:
    proc_pool = ProcessPoolExecutor(cpu_count())
    thread_pool = ThreadPoolExecutor(cpu_count())
    
    def proc(self, method: str, *args: Any): return self.proc_pool.submit(rpc_call, method, *args)
    def thread(self, method: str, *args: Any): return self.thread_pool.submit(rpc_call, method, *args)
    def mProc(self, *args: Any): return self.proc_pool.map(rpc_call, *args)
    def mThread(self, *args: Any): return self.thread_pool.map(rpc_call, args)
    

def rpcProc(method: str, *args: Any):
    with ProcessPoolExecutor(cpu_count()) as tpe: return tpe.submit(rpc_call, method, args)


def rpcThread(method: str, *args: Any):
    with ThreadPoolExecutor(cpu_count()) as tpe: return tpe.submit(rpc_call, method, args)


def rpcMProc(method: str, *args: Any):
    with ProcessPoolExecutor(cpu_count()) as tpe: return tpe.map(rpc_call, method, args)


def rpcMThread(method: str, *args: Any):
    with ThreadPoolExecutor(cpu_count()) as tpe: return tpe.map(lambda p: rpc_call(method, p), args)