from os.path import join
from platform import system
from pathlib import Path
from typing import TypeAlias


ip: TypeAlias= str
ips: TypeAlias = list[str]

chain: str = 'raven'
Chain: str = chain.capitalize()
def get_default_path():
    home = Path.home()
    platform = ['Linux', 'Mac']
    operating_system = system()
    if operating_system is platform[0]:
        return join(home, f'.{chain}')
    elif operating_system is platform[1]:
        return join(home, 'Library', 'Application', 'Support', Chain)
    else: return join(home, 'AppData', 'Roaming', Chain)


default_path = get_default_path()


def generate_conf(
    testnet: int=None, regtest: int=None, proxy: ip=None, bind: ip=None, whitebind: ip=None, nodes: ips=None, connections: ips=None, listen=1, maxconnections: int=None,           # type: ignore
    server: int=1, rpcbinds: ips=None, authentications: list[str]=None, rpcuser: str='user', rpcpassword: str='pass', rpcclienttimeout=30, rpcallowedips: list=['127.0.0.1'],      # type: ignore
    zmqpub: str=None, rpcport: int=8766, wallet: str=default_path, datadir: str=default_path, rpcconnect: ip='127.0.0.1', txconfirmtarget=6, keypool=100, paytxfee: float=None,    # type: ignore
    prune: int=0, minimized=0, totray=1, txindex=1, addressindex=1, assetindex=1, timestampindex=1, spentindex=1 
):
    testnet = testnet if testnet else 0
    regtest = regtest if regtest else 0
    proxy = f'proxy={proxy}\n' if proxy else '#proxy=\n'
    bind = f'bind={bind}\n' if bind else '#bind=\n'
    whitebind = f'whitebind={whitebind}\n' if whitebind else f'#whitebind=\n'
    addnode = [f'addnode={node}\n' for node in nodes] if nodes else '#addnode=\n'
    connect = [f'connect={connection}\n' for connection in connections] if connections else '#connect=\n'
    maxconnections = f'maxconnections={maxconnections}\n' if maxconnections else '#maxconnections=\n'                                                                              # type: ignore
    rpcbind = [f'rpcbind={bind}\n' for bind in rpcbinds] if rpcbinds else '#rpcbind=\n'
    rpcauth = [f'rpcauth={auth}\n' for auth in authentications] if authentications else '#rpcauth=\n'
    rpcallowip = [f'rpcallowip={rpcallowip}\n' for rpcallowip in rpcallowedips]
    node_ip = f'tcp://{zmqpub}:28767' if zmqpub else None
    zmqpubrawtx = f'zmqpubrawtx={node_ip}\n' if node_ip else f'#zmqpubrawtx=\n'
    zmqpubrawblock = f'zmqpubrawblock={node_ip}\n' if node_ip else f'#zmqpubrawblock=\n'
    zmqpubhashtx = f'zmqpubhashtx={node_ip}\n' if node_ip else '#zmqpubhashtx=\n'
    zmqpubhashblock = f'zmqpubhashblock={node_ip}\n' if node_ip else '#zmqpubhashblock=\n'
    paytxfee = f'paytxfee={paytxfee}\n' if paytxfee else '#paytxfee=\n'                                                                                                            # type: ignore


    with open(join(default_path, f'{chain}.conf'), 'w') as file:
        ws = ' '
        hl = '#' * 62
        settings = [
            '##\n', f'## {chain}.conf configuration file. Lines beginning with # are comments.\n', '##\n', '\n', '# Network-related settings:\n', 
            '\n', f'# Run on the test network instead of the real {chain} network.\n', f'testnet={testnet}\n', 
            '\n', '# Run a regression test network\n', f'regtest={regtest}\n', '\n', '# Connect via a SOCKS5 proxy\n', proxy, '\n',
            '# Bind to given address and always listen on it. Use [host]:port notation for IPv6\n',
            bind, '\n', '# Bind to given address and whitelist peers connecting to it. Use [host]:port notation for IPv6\n',
            whitebind, '\n', f'{hl}\n', f'##{ws*12}Quick Primer on addnode vs connect{ws*12}##\n',
            f'##  Let\'s say for instance you use addnode=4.2.2.4{ws*10}##\n', f'##  addnode will connect you to and tell you about the{ws*6}##\n',
            '##    nodes connected to 4.2.2.4.  In addition it will tell ##\n', '##    the other nodes connected to it that you exist so     ##\n',
            f'##    they can connect to you.{ws*30}##\n', '##  connect will not do the above when you \'connect\' to it. ##\n',
            '##    It will *only* connect you to 4.2.2.4 and no one else.##\n', f'##{ws*58}##\n', '##  So if you\'re behind a firewall, or have other problems  ##\n',
            f'##  finding nodes, add some using \'addnode\'.{ws*16}##\n', f'##{ws*58}##\n', '##  If you want to stay private, use \'connect\' to only      ##\n',
            f'##  connect to "trusted" nodes.{ws*29}##\n', f'##{ws*58}##\n', '##  If you run multiple nodes on a LAN, there\'s no need for ##\n',
            f'##  all of them to open lots of connections.  Instead{ws*7}##\n', '##  \'connect\' them all to one node that is port forwarded   ##\n',
            f'##  and has lots of connections.{ws*28}##\n', f'##       Thanks goes to [Noodle] on Freenode.{ws*15}##\n',
            f'{hl}\n', '# Use as many addnode= settings as you like to connect to specific peers\n',
            *addnode, '\n', '# Alternatively use as many connect= settings as you like to connect ONLY to specific peers\n',
            *connect, '\n', '# Listening mode, enabled by default except when \'connect\' is being used\n',
            f'listen={listen}\n', '\n', '# Maximum number of inbound+outbound connections.\n',
            maxconnections, '\n', '#\n', f'# JSON-RPC options (for controlling a running {Chain}/{chain}d process)\n',
            '#\n', '\n', f'# server=1 tells {Chain}-Qt and {chain}d to accept JSON-RPC commands\n', f'server={server}\n',
            '\n', '# Bind to given address to listen for JSON-RPC connections. Use [host]:port notation for IPv6.\n',
            '# This option can be specified multiple times (default: bind to all interfaces)\n',
            *rpcbind, '\n', '# If no rpcpassword is set, rpc cookie auth is sought. The default `-rpccookiefile` name\n',
            f'# is .cookie and found in the `-datadir` being used for {chain}d. This option is typically used\n',
            '# when the server and client are run as the same user.\n', '#\n',
            '# If not, you must set rpcuser and rpcpassword to secure the JSON-RPC api. The first\n',
            '# method (DEPRECATED) is to set this pair for the server and client:\n',
            '# rpcuser=Ulysseys\n', '# rpcpassword=YourSuperGreatPasswordNumber_DO_NOT_USE_THIS_OR_YOU_WILL_GET_ROBBED_385593\n',
            '#\n', '# The second method `rpcauth` can be added to server startup argument. It is set at initialization time\n',
            '# using the output from the script in share/rpcuser/rpcuser.py after providing a username:\n',
            '#\n', '# ./share/rpcuser/rpcuser.py alice\n', f'# String to be appended to {chain}.conf:\n',
            '# rpcauth=alice:f7efda5c189b999524f151318c0c86$d5b51b3beffbc02b724e5d095828e0bc8b2456e9ac8757ae3211a5d9b16a22ae\n',
            '# Your password:\n', '# DONT_USE_THIS_YOU_WILL_GET_ROBBED_8ak1gI25KFTvjovL3gAM967mies3E=\n',
            '#\n', '# On client-side, you add the normal user/password pair to send commands:\n',
            '# rpcuser=alice\n', '# rpcpassword=DONT_USE_THIS_YOU_WILL_GET_ROBBED_8ak1gI25KFTvjovL3gAM967mies3E=\n',
            '#\n', '# You can even add multiple entries of these to the server conf file, and client can use any of them:\n',
            '# rpcauth=bob:b2dd077cb54591a2f3139e69a897ac$4e71f08d48b4347cf8eff3815c0e25ae2e9a4340474079f55705f40574f4ec99\n',
            '\n', *rpcauth, '\n', f'rpcuser={rpcuser}\n', f'rpcpassword={rpcpassword}\n', '\n',
            f'# How many seconds {chain} will wait for a complete RPC HTTP request.\n',
            '# after the HTTP connection is established.\n', f'rpcclienttimeout={rpcclienttimeout}\n',
            '\n', '# By default, only RPC connections from localhost are allowed.\n',
            '# Specify as many rpcallowip= settings as you like to allow connections from other hosts,\n',
            '# either as a single IPv4/IPv6 or with a subnet specification.\n',
            '\n', '# NOTE: opening up the RPC port to hosts outside your local trusted network is NOT RECOMMENDED,\n',
            '# because the rpcpassword is transmitted over the network unencrypted.\n',
            '\n', f'# server=1 tells {Chain}-Qt to accept JSON-RPC commands.\n', f'# it is also read by {chain}d to determine if RPC should be enabled \n',
            *rpcallowip, '\n', '# Enable zeromq for real-time data\n', zmqpubrawtx, zmqpubrawblock, zmqpubhashtx, zmqpubhashblock, '\n', 
            '# Listen for RPC connections on this TCP port:\n', f'rpcport={rpcport}\n', '\n', f'# You can use {Chain} or {chain}d to send commands to {Chain}/{chain}d\n',
            '# running on another host using this option:\n', f'rpcconnect={rpcconnect}\n',
            '\n', '# Create transactions that have enough fees so they are likely to begin confirmation within n blocks (default: 6).\n',
            '# This setting is over-ridden by the -paytxfee option.\n', f'txconfirmtarget={txconfirmtarget}\n', '\n',
            '# Wallet options\n', '\n', '# Specify where to find wallet, lockfile and logs. If not present, those files will be\n',
            '# created as new.\n', f'wallet={wallet}\n', f'datadir={datadir}\n', '\n', '# Miscellaneous options\n', '\n',
            '# Pre-generate this many public/private key pairs, so wallet backups will be valid for\n',
            '# both prior transactions and several dozen future transactions.\n', f'keypool={keypool}\n', '\n', 
            f'# Pay an optional transaction fee every time you send {chain}s. Transactions with fees\n',
            '# are more likely than free transactions to be included in generated blocks, so may\n', '# be validated sooner.\n', paytxfee, 
            '\n', '# Enable pruning to reduce storage requirements by deleting old blocks.\n', '# This mode is incompatible with -txindex and -rescan.\n', 
            '# 0 = default (no pruning).\n', '# 1 = allows manual pruning via RPC.\n', '# >=550 = target to stay under in MiB.\n', f'prune={prune}\n', '\n', 
            '# User interface options\n', '\n', f'# Start {Chain} minimized\n', f'min={minimized}\n', '\n', '# Minimize to the system tray\n', f'minimizetotray={totray}\n', '\n',
            '# Maintains the full Transaction index on your node. Needed if you call getrawtransaction. Default is 0.\n',
            f'txindex={txindex}\n', '\n', '# Maintains the full Address index on your node. Needed if you call getaddress* calls. Default is 0.\n',
            f'addressindex={addressindex}\n', '\n', '# Maintains the full Asset index on your node. Needed if you call getassetdata. Default is 0.\n',
            f'assetindex={assetindex}\n', '\n', '# Maintains the full Timestamp index on your node. Default is 0.\n', f'timestampindex={timestampindex}\n', '\n', 
            '# Maintains the full Spent index on your node. Default is 0.\n', f'spentindex={spentindex}'
        ]
        file.writelines(settings)

if __name__ == '__main__':
    generate_conf()