from __future__ import annotations
from os import cpu_count
import asyncio
from asyncio import Queue, create_task
from httpx import AsyncClient
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


class DispatchRPC:
    def __init__(self,
        username: str,
        password: str,
        port: str,
        client: AsyncClient,
        workers: int = 5,
        limit: int = 10
    ) -> None:
        self.client = client
        self.num_workers = workers
        self.limit = limit
        self.total = 0
        def __call__(method, *args):
            url = f'http://localhost:{port}'
            json = {'jsonrpc': '1.0', 'id': 'python', 'method': method, 'params': args}
            return client.post(url, json=json, auth=(username, password))
    
    async def run(self): pass
    

async def main(username, password, *args, **kwrg):
    async with AsyncClient() as client:
        with ThreadPoolExecutor(cpu_count()) as exec: pass
        with ProcessPoolExecutor(cpu_count()) as exec: pass
        auth = (username, password)


if __name__ == '__main__': 
    asyncio.run(main('geblockchaininfo', [], 8770))