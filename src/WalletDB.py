import pickledb
from mnemonic import Mnemonic
from hdwallet import HDWallet, BIP141HDWallet
from hdwallet.symbols import RVN
from hdwallet.cryptocurrencies import get_cryptocurrency
from src.Database import settings

class Wallet:
    def __init__(self, symbol: str, phrase: str, account: str) -> None:
        self.chindex = 0
        self.symbol = symbol
        self.mnemonic = phrase
        self.account = account
        self.accindex = int(account.split('.')[-1])
        self.db = pickledb.load(f'src/Database/wallets/{symbol.lower()}-wallet-{self.accindex}.json', True)
        if not self.db.exists(account): self.db.lcreate(account); self.db.dump()
        self.lenaddrs = self.db.llen(account)
        self.listaddrs = list(self.db.lgetall(account))
        self.lenkeys = self.db.totalkeys()
        self.keys = list(self.db.getall())
        self.language = settings['language']
        self.password = settings['password']
        
    def generate_mnemonics(self, amount, offset=0):
        mndb = pickledb.load('src/Database/mnemonic.json', True)
        for i in range(amount):
            name = f'wallet.{i + offset}'
            if not mndb.exists(name): mndb.lcreate(name)
            new_mnem = Mnemonic(self.language).generate()
            mndb.append(name, [new_mnem])

    def get_wallet(self, accindex, addrindex=0) -> HDWallet:
        wallet = BIP141HDWallet(self.symbol, get_cryptocurrency(self.symbol), f"m/44'/175'/{accindex}'/{self.chindex}/{addrindex}")
        return wallet.from_mnemonic(self.mnemonic, self.language, self.password)

    def get_wallets(self, accindex, amount, offset=0) -> list[HDWallet]: return [
        self.get_wallet(accindex, i + offset) for i in range(amount)]

    def generate_addresses(self, amount=1):
        wallets = self.get_wallets(int(self.account.split('.')[1]), amount, self.lenaddrs)
        addresses = [wallet.p2pkh_address() for wallet in wallets]
        if not self.db.exists(self.account): self.db.lcreate(self.account)
        if self.db.append(self.account, addresses): return addresses