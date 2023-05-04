from requests import post


async def get_data(*args, **kwargs):
    def make_payload(): method, params = args; return {'method': method, 'params': params}
    def get_url():
        if (key := 'testing') in kwargs: testing = kwargs[key]
        else: testing = False
        if testing: url = 'https://rvn-rpc-testnet.ting.finance/rpc'
        else: url = 'https://rvn-rpc-mainnet.ting.finance/rpc'
        return url
    return result if (r := 'result') in (result := post(get_url(), json=make_payload()).json()[r]) else {result}


def get_address_balance(*args, **kwargs):
    if (key := 'include_assets') in kwargs: include_assets = kwargs[key]
    else: include_assets = False
    return get_data('getaddressbalance', [{'addresses': [*args]}, include_assets])


def get_address_txids(*args, **kwargs): 
    if (key := 'include_assets') in kwargs: include_assets = kwargs[key]
    else: include_assets = False
    return get_data('getaddresstxids', [{'addresses': [*args]}, include_assets])


def get_address_utxos(*args, **kwargs):
    if (key := 'chain_info') in kwargs: chain_info = kwargs[key]
    else: chain_info = False
    if (key := 'asset_name') in kwargs: asset_name = kwargs[key]
    else: asset_name = 'RVN'
    return get_data('getaddressutxos', [{'addresses': [*args], 'chainInfo': chain_info, 'assetName': asset_name}])


def is_valid(*args): return get_data('validateaddress', [*args])


def create_raw_transaction(*args): inputs, outputs = args; return get_data('createrawtransaction', [inputs, outputs])


def sign_message(*args): privkey, message = args; return get_data('signmessagewithprivkey', [privkey, message])


def verify_message(*args): address, signature, message = args; return get_data('verifymessage', [address, signature, message])