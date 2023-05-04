# from requests import post
from httpx import Client
from src.Database.params import commands

class Call:
    def __init__(self, username, password, port) -> None:
        self.cli = Client(
            auth = (username, password),
            headers = {'content-type': 'application/json'}
        )
        self.__call__: function = lambda method, parameters: self.cli.post(
            f'http://localhost:{port}', 
            json = {
                'jsonrpc': '1.0',
                'id': 'python',
                'method': method,
                'params': list(parameters)
            }
        ).json()['result']
        __all__ = commands     
    def __dir__(self): return commands
    def __call__(self, method: str, *args) -> dict: # type: ignore
        return self.__call__(method, list(args))
    
    def __getattr__(self, method: str):
        def command(*args): return self.__call__(method, list(args))
        return command
      

def get_address_utxos(rpc: Call, addresses: list, 
    chain_info: bool | None=None, asset_name: str | None=None
    ):
    payload = {
        'addresses': [
            *addresses
        ],
        'chainInfo': chain_info,
        'assetName': asset_name
    }
    return rpc.getaddressutxos(payload)


def create_raw_transaction(rpc: Call, inputs: list, outputs: dict, 
        locktime: int | None=None
    ) -> str:
    return rpc.createrawtransaction(inputs, outputs, locktime)


def sign_message(rpc: Call, wif: str, message: str) -> str: 
    return rpc.signmessagewithprivkey(wif, message)


def verify_message(rpc: Call, address: str, signature: str, message: str) -> bool: 
    return rpc.verifymessage(address, signature, message)
