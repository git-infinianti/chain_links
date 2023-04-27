from requests import post
from src.chain_params import commands


class RPC:
    def __init__(self, username, password, port) -> None:
        self.__call__: function = lambda method, parameters: post(
            f'http://localhost:{port}', 
            json = {
            'jsonrpc': '1.0',
            'id': 'python',
            'method': method,
            'params': parameters,
            }, 
            auth = (username, password)
        ).json()['result']

    def __call__(self, method: str, *args) -> dict: # type: ignore
        return self.__call__(method, list(args))
    
    def __getattr__(self, method: str):
        def command(*args): return self.__call__(method, list(args))
        return command
    
    def __dir__(self): return commands


def get_address_utxos(rpc: RPC, addresses: list, 
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


def create_raw_transaction(rpc: RPC, inputs: list, outputs: dict, 
        locktime: int | None=None
    ) -> str:
    return rpc.createrawtransaction(inputs, outputs, locktime)


def sign_message(rpc: RPC, wif: str, message: str) -> str: 
    return rpc.signmessagewithprivkey(wif, message)


def verify_message(rpc: RPC, address: str, signature: str, message: str) -> bool: 
    return rpc.verifymessage(address, signature, message)


def inputs(txids: list, vouts: list, sequences: list | None=None):
    def _input(txid, vout, sequence=None):
        return {'txid': txid, 'vout': vout, 'sequence': sequence}
    return [
        _input(txid, vout, sequence) 
        for txid, vout, sequence 
        in zip(txids, vouts, sequences) 
    ] if sequences else [
        _input(txid, vout) 
        for txid, vout 
        in zip(txids, vouts)]


def outputs(addresses: list, amounts: list):
    return {address: amount for address, amount in zip(addresses, amounts)}