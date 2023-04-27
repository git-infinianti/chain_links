from os import path
from json import load
from hdwallet import BIP44HDWallet
from hdwallet.symbols import RVN
from hdwallet.cryptocurrencies import Cryptocurrency, get_cryptocurrency


data_dir = path.join('./.data/', 'settings.json')
with open(data_dir, 'r') as file:
    SETTINGS = load(file)
    LANGUAGE = SETTINGS['language']
    PASSWORD = SETTINGS['password']

data_dir = path.join('./.data/', 'mnemonic.json')
with open(data_dir, 'r') as file:
    PHRASE = load(file)[0]


class Wallet:
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.currency: Cryptocurrency = get_cryptocurrency(symbol)
        
    def get_address(self, address=0, change=False, account=0):
        bip44_hdwallet = BIP44HDWallet(
            self.symbol, self.currency, account, change, address
        )
        bip44_hdwallet.from_mnemonic(PHRASE, LANGUAGE, PASSWORD)
        return bip44_hdwallet.p2pkh_address()