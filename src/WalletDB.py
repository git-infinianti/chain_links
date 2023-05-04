from os import cpu_count, listdir
from datetime import datetime, timezone
from concurrent.futures import ProcessPoolExecutor, as_completed
from typing import Any

import pickledb
from mnemonic import Mnemonic
from hdwallet import HDWallet, BIP141HDWallet
from hdwallet.cryptocurrencies import get_cryptocurrency

from src.RPC import Call
from src.Database import settings


def unix_to_time(unix_timestamp):
    dt = datetime.fromtimestamp(unix_timestamp, timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def get_time(dt): return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


def generate_mnemonics(wallet, amount: int, single=True, offset=0):
    mndb = pickledb.load('src/Database/mnemonic.json', True)
    for i in range(amount):
        name = wallet if single else f'wallet.{i + offset}'
        if not mndb.exists(name):
            mndb.lcreate(name)
        new_mnem = Mnemonic(settings['language']).generate()
        mndb.append(name, [new_mnem])


class Wallet:
    def __init__(self, symbol: str, wallet: str, account: str, phrase: str) -> None:
        self.changeIndex = 0
        self.symbol = symbol.upper()
        self.wallet = wallet
        self.mnemonic = phrase
        self.account = account
        def get_index(name): return int(name.split('.')[-1])
        self.walletIndex = get_index(wallet)
        self.accountIndex = get_index(account)
        self.db = pickledb.load(
            f'src/Database/wallets/{symbol.lower()}_wallet_{self.walletIndex}.json', True)
        if not self.db.exists(account):
            self.db.lcreate(account)
            self.db.dump()
        self.keys = list(self.db.getall())
        self.lenkeys = self.db.totalkeys()
        self.lenaddrs = self.db.llen(account)
        self.listAddrs = list(self.db.lgetall(account))
        self.language = settings['language']
        self.password = settings['password']

    def get_wallet(self, accindex, addrindex=0) -> HDWallet:
        wallet = BIP141HDWallet(self.symbol, get_cryptocurrency(
            self.symbol), f"m/44'/175'/{accindex}'/{self.changeIndex}/{addrindex}")
        return wallet.from_mnemonic(self.mnemonic, self.language, self.password)

    def get_wallets(self, accindex, amount, offset=0):
        with ProcessPoolExecutor(cpu_count()) as executor:
            futrs = [executor.submit(
                self.get_wallet, accindex, i + offset) for i in range(amount)]
            for futr in futrs:
                yield futr.result()

    def generate_addresses(self, amount=1):
        if not self.db.exists(self.account):
            self.db.lcreate(self.account)
        wallets = self.get_wallets(
            int(self.account.split('.')[1]), amount, self.lenaddrs)

        def addresses():
            for wallet in wallets:
                yield wallet.p2pkh_address()
        addrs = addresses()
        self.db.append(self.account, list(addrs))
        return addrs


def bip32hdkeypath(address=0, change=0, account=0):
    return f"m/{account}'/{change}'/{address}'"


def bip44hdkeypath(address=0, change=0, account=0):
    return f"m/44'/175'/{account}'/{change}/{address}"


class CoreWalletDump:
    def __init__(self, softwareVersion: str, symbol: str, rpc: Call, mnemonic: str) -> None:
        self.rpc = rpc
        self.symbol = symbol
        self.filename = 'wallet'
        self.bip44 = False
        self.changeIndex = 0
        self.accountIndex = 0
        self.mnemonic = mnemonic
        self.softwareVersion = softwareVersion
        self.wallet = self.get_wallet()

    def __call__(self, address=0):
        self.addressIndex = address
        self.wallet = self.get_wallet(address)
        return self.wallet

    def get_wallet(self, address=0):
        keypath = bip44hdkeypath(
            address, self.changeIndex, self.accountIndex
        ) if self.bip44 else bip32hdkeypath(
            address, self.changeIndex, self.accountIndex
        )
        wallet = BIP141HDWallet(self.symbol, get_cryptocurrency(self.symbol), keypath)
        return wallet.from_mnemonic(self.mnemonic, settings['language'], settings['password'])

    def wallet_boiler(self):
        chainInfo = self.rpc.getblockchaininfo()
        block = chainInfo['blocks']
        blockHash = chainInfo['bestblockhash']
        getTime = get_time(datetime.utcnow())
        toTime = unix_to_time(chainInfo['mediantime'])
        return [
            f'# Wallet dump created by {self.softwareVersion}\n',
            f'# * Created on {getTime}\n',
            f'# * Best block at time of backup was {block} ({blockHash}),\n',
            f'#   mined on {toTime}\n\n',
            f'# extended private masterkey: {self.wallet.root_xprivate_key()}\n\n'
        ]

    def wallet_dump(self, key='label', value=''):
        wallet = self.wallet
        return f"{wallet.wif()} {get_time(datetime.utcnow())} {key}={value} # {wallet.p2pkh_address()} hdkeypath={wallet.path()}\n"

    def wallet_dumps(self, amount=1, dumpData: list = []):
        file = f'{self.filename}.dat'
        try:
            if file in listdir(): raise FileExistsError
            dumpData = []
            for i in range(amount):
                self(i)
                dumpData.append(self.wallet_dump())
            return dumpData
        except FileExistsError:
            with ProcessPoolExecutor(cpu_count()) as executor:
                with open(file, 'r') as file:
                    lines = file.readlines()[7:-2]
                    futures = [executor.submit(dumpData.remove, line) for line in lines if line in dumpData]
                for future in as_completed(futures): future.result()
                newData = lines + dumpData
                offset = len(newData)
                for i in range(amount):
                    self(i + offset)
                    newData.append(self.wallet_dump())
                return newData

    def dump_wallet(self, dumpData: list):
        dumpEnd = '\n# End of dump'
        with open(f'{self.filename}.dat', 'w') as file:
            dumpData.append(dumpEnd)
            file.writelines(self.wallet_boiler() + dumpData)


if __name__ == '__main__':
    from os import getenv
    from dotenv import load_dotenv
    load_dotenv()
    acc = 4
    mnem = str(getenv('MNEM'))
    sftwrV = 'Foxdcoin v1.1.0.1-9db505f-dirty'
    rpc = Call(getenv('RPCUSER'), getenv('RPCPASS'), 8770)
    coreDump = CoreWalletDump(sftwrV, 'FOXD', rpc, mnem)
    coreDump.bip44 = True
    coreDump.filename = f'account-{acc}'
    coreDump.accountIndex = acc
    dumpData = coreDump.wallet_dumps(100)
    coreDump.dump_wallet(dumpData)
