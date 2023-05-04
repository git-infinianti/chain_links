from typing import Any
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
        def command(*args): return self(method, list(args))
        return command

    def get_address_utxos(self, 
        addresses: list, chain_info: bool | None=None, 
        asset_name: str | None=None
        ) -> dict:
        payload = {
            'addresses': [*addresses],
            'chainInfo': chain_info,
            'assetName': asset_name
        }
        return self.getaddressutxos(payload)

    def create_raw_transaction(self,
            inputs: list[dict[str, str]], outputs: dict[str, str | float | dict[str, Any]],
            locktime: int | None=None
        ) -> str:
        return self.createrawtransaction(inputs, outputs, locktime)

    def sign_message(self, wif: str, message: str) -> str:     
        return self.signmessagewithprivkey(wif, message)

    def verify_message(self, address: str, signature: str, message: str) -> bool: 
        return self.verifymessage(address, signature, message)
