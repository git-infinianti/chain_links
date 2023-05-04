from hdwallet.cryptocurrencies import *


class Ravencoin(RavencoinMainnet):
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "ra",
        "VERSION": 0x0c
    })


class RavencoinTestnet(Cryptocurrency):
    NAME = "Ravencoin"
    SYMBOL = "RVNTEST"
    NETWORK = "testnet"
    SOURCE_CODE = "https://github.com/RavenProject/Ravencoin"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tr",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x04358394,
        "P2WPKH_IN_P2SH": 0x04358394,
        "P2WSH": 0x04358394,
        "P2WSH_IN_P2SH": 0x04358394
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x043587cf,
        "P2WPKH_IN_P2SH": 0x043587cf,
        "P2WSH": 0x043587cf,
        "P2WSH_IN_P2SH": 0x043587cf
    })

    MESSAGE_PREFIX = "Raven Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class EvrcoinMainnet(Cryptocurrency):
    NAME = "Evrcoin"
    SYMBOL = "EVR"
    NETWORK = "mainnet"
    SOURCE_CODE = "https://github.com/EvrmoreOrg/Evrmore"
    COIN_TYPE = CoinType({
        "INDEX": 175,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5c
    PUBLIC_KEY_ADDRESS = 0x21
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "ev",
        "VERSION": 0x03
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })

    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })
    
    MESSAGE_PREFIX = "Evrmore Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class EvrcoinTestnet(Cryptocurrency):
    NAME = "Evrcoin"
    SYMBOL = "EVRTEST"
    NETWORK = "testnet"
    SOURCE_CODE = "https://github.com/EvrmoreOrg/Evrmore"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0xc4
    PUBLIC_KEY_ADDRESS = 0x6f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "te",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x04358394,
        "P2SH": 0x04358394,
        "P2WPKH": 0x045f18bc,
        "P2WPKH_IN_P2SH": 0x044a4e28,
        "P2WSH": 0x02575048,
        "P2WSH_IN_P2SH": 0x024285b5
    })

    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x043587cf,
        "P2SH": 0x043587cf,
        "P2WPKH": 0x045f1cf6,
        "P2WPKH_IN_P2SH": 0x044a5262,
        "P2WSH": 0x02575483,
        "P2WSH_IN_P2SH": 0x024289ef
    })
    
    MESSAGE_PREFIX = "Evrmore Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class FoxdcoinMainnet(Cryptocurrency):
    NAME = "Foxdcoin"
    SYMBOL = "FOXD"
    NETWORK = "mainnet"
    SOURCE_CODE = "https://github.com/foxdproject/foxdcoin"
    COIN_TYPE = CoinType({
        "INDEX": 175,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x1e
    PUBLIC_KEY_ADDRESS = 0x23
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "fx",
        "VERSION": 0x0d
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })

    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })

    MESSAGE_PREFIX = "Foxdcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


class FoxdcoinTestnet(Cryptocurrency):
    NAME = "Foxdcoin"
    SYMBOL = "FOXDTEST"
    NETWORK = "testnet"
    SOURCE_CODE = "https://github.com/foxdproject/foxdcoin"
    COIN_TYPE = CoinType({
        "INDEX": 1,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x5a
    PUBLIC_KEY_ADDRESS = 0x5f
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "tf",
        "VERSION": 0x00
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })
    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })
    
    MESSAGE_PREFIX = "Foxdcoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0xef


class AviancoinMainnet(Cryptocurrency):
    NAME = "Aviancoin"
    SYMBOL = "AVN"
    NETWORK = "mainnet"
    SOURCE_CODE = "https://github.com/AvianNetwork/Avian"
    COIN_TYPE = CoinType({
        "INDEX": 921,
        "HARDENED": True
    })

    SCRIPT_ADDRESS = 0x7a
    PUBLIC_KEY_ADDRESS = 0x3c
    SEGWIT_ADDRESS = SegwitAddress({
        "HRP": "av",
        "VERSION": 0x04
    })

    EXTENDED_PRIVATE_KEY = ExtendedPrivateKey({
        "P2PKH": 0x488ade4,
        "P2SH": 0x488ade4,
        "P2WPKH": 0x04b2430c,
        "P2WPKH_IN_P2SH": 0x049d7878,
        "P2WSH": 0x02aa7a99,
        "P2WSH_IN_P2SH": 0x0295b005
    })

    EXTENDED_PUBLIC_KEY = ExtendedPublicKey({
        "P2PKH": 0x488b21e,
        "P2SH": 0x488b21e,
        "P2WPKH": 0x04b24746,
        "P2WPKH_IN_P2SH": 0x049d7cb2,
        "P2WSH": 0x02aa7ed3,
        "P2WSH_IN_P2SH": 0x0295b43f
    })
    
    MESSAGE_PREFIX = "Aviancoin Signed Message:\n"
    DEFAULT_PATH = f"m/44'/{str(COIN_TYPE)}/0'/0/0"
    WIF_SECRET_KEY = 0x80


def get_cryptocurrency(symbol: str) -> Any:
    for _, cryptocurrency in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(cryptocurrency):
            if issubclass(cryptocurrency, Cryptocurrency) and cryptocurrency != Cryptocurrency:
                if symbol == cryptocurrency.SYMBOL:
                    return cryptocurrency
    raise ValueError(f"Invalid Cryptocurrency '{symbol}' symbol.")