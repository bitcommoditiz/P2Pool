import os
import platform

from twisted.internet import defer

from . import data
from p2pool.util import math, pack

nets = dict(
    xauz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55884,#ICI
        ADDRESS_VERSION=38,#ICI
        RPC_PORT=55883,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'XAUzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='XAUz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'XAUz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/XAUz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.XAUz'), 'XAUz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://xauz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://xauz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://xauz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    xpdz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55886,#ICI
        ADDRESS_VERSION=55,#ICI
        RPC_PORT=55885,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'XPDzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='XPDz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'XPDz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/XPDz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.XPDz'), 'XPDz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://xpdz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://xpdz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://xpdz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    xagz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55888,#ICI
        ADDRESS_VERSION=63,#ICI
        RPC_PORT=55887,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'XAGzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='XAGz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'XAGz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/XAGz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.XAGz'), 'XAGz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://xagz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://xagz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://xagz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    xptz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55890,#ICI
        ADDRESS_VERSION=56,#ICI
        RPC_PORT=55889,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'XPTzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='XPTz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'XPTz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/XPTz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.XPTz'), 'XPTz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://xptz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://xptz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://xptz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    clz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55892,#ICI
        ADDRESS_VERSION=48,#ICI
        RPC_PORT=55891,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'CLzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='CLz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CLz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CLz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CLz'), 'CLz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://clz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://clz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://clz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    wz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55894,#ICI
        ADDRESS_VERSION=73,#ICI
        RPC_PORT=55893,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'Wzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='Wz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Wz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Wz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.Wz'), 'Wz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://wz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://wz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://wz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    zcz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55896,#ICI
        ADDRESS_VERSION=30,#ICI
        RPC_PORT=55895,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'ZCzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='ZCz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'ZCz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/ZCz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.ZCz'), 'ZCz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://zcz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://zcz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://zcz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    ctz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55898,#ICI
        ADDRESS_VERSION=33,#ICI
        RPC_PORT=55897,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'CTzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='CTz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CTz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CTz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CTz'), 'CTz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://ctz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://ctz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://ctz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    kcz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55900,#ICI
        ADDRESS_VERSION=35,#ICI
        RPC_PORT=55899,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'KCzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='KCz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'KCz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/KCz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.KCz'), 'KCz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://kcz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://kcz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://kcz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    ccz=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),#Litecoin P2P prefix
        P2P_PORT=55902,#ICI
        ADDRESS_VERSION=23,#ICI
        RPC_PORT=55901,#ICI
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'CCzaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 1*100000000 >> (height + 1)//840000,#ICI cf subsidy 
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=300, # s (5 min)
        SYMBOL='CCz',#ICI
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'CCz') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/CCz/') if platform.system() == 'Darwin' else os.path.expanduser('~/.CCz'), 'CCz.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://ccz.blockchain.bitcommoditiz.org/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://ccz.blockchain.bitcommoditiz.org/address/',
        TX_EXPLORER_URL_PREFIX='http://ccz.blockchain.bitcommoditiz.org/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1), #The SANE_TARGET_RANGE is what limits the range of served shares.  The max/min is the same number (which equates to diff 1). You would need to edit this range to allow for higher difficulty shares.
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    bitcoin=math.Object(
        P2P_PREFIX='f9beb4d9'.decode('hex'),
        P2P_PORT=8333,
        ADDRESS_VERSION=0,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='BTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='https://blockchain.info/block/',
        ADDRESS_EXPLORER_URL_PREFIX='https://blockchain.info/address/',
        TX_EXPLORER_URL_PREFIX='https://blockchain.info/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.001e8,
    ),
    bitcoin_testnet=math.Object(
        P2P_PREFIX='0b110907'.decode('hex'),
        P2P_PORT=18333,
        ADDRESS_VERSION=111,
        RPC_PORT=18332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'bitcoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='tBTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.bitcoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://blockexplorer.com/testnet/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    
    namecoin=math.Object(
        P2P_PREFIX='f9beb4fe'.decode('hex'),
        P2P_PORT=8334,
        ADDRESS_VERSION=52,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'namecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='NMC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Namecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Namecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.namecoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/b/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/a/',
        TX_EXPLORER_URL_PREFIX='http://explorer.dot-bit.org/tx/',
        SANE_TARGET_RANGE=(2**256//2**32 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=0.2e8,
    ),
    namecoin_testnet=math.Object(
        P2P_PREFIX='fabfb5fe'.decode('hex'),
        P2P_PORT=18334,
        ADDRESS_VERSION=111,
        RPC_PORT=8332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'namecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//210000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=600, # s
        SYMBOL='tNMC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Namecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Namecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.namecoin'), 'bitcoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/b/',
        ADDRESS_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/a/',
        TX_EXPLORER_URL_PREFIX='http://testnet.explorer.dot-bit.org/tx/',
        SANE_TARGET_RANGE=(2**256//2**32 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    
    litecoin=math.Object(
        P2P_PREFIX='fbc0b6db'.decode('hex'),
        P2P_PORT=9333,
        ADDRESS_VERSION=48,
        RPC_PORT=9332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'litecoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='LTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Litecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Litecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.litecoin'), 'litecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/address/',
        TX_EXPLORER_URL_PREFIX='http://explorer.litecoin.net/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256//1000 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=0.03e8,
    ),
    litecoin_testnet=math.Object(
        P2P_PREFIX='fcc1b7dc'.decode('hex'),
        P2P_PORT=19333,
        ADDRESS_VERSION=111,
        RPC_PORT=19332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'litecoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 50*100000000 >> (height + 1)//840000,
        POW_FUNC=lambda data: pack.IntType(256).unpack(__import__('ltc_scrypt').getPoWHash(data)),
        BLOCK_PERIOD=150, # s
        SYMBOL='tLTC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Litecoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Litecoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.litecoin'), 'litecoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/address/',
        TX_EXPLORER_URL_PREFIX='http://nonexistent-litecoin-testnet-explorer/tx/',
        SANE_TARGET_RANGE=(2**256//1000000000 - 1, 2**256 - 1),
        DUMB_SCRYPT_DIFF=2**16,
        DUST_THRESHOLD=1e8,
    ),

    terracoin=math.Object(
        P2P_PREFIX='42babe56'.decode('hex'),
        P2P_PORT=13333,
        ADDRESS_VERSION=0,
        RPC_PORT=13332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='TRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),
    terracoin_testnet=math.Object(
        P2P_PREFIX='41babe56'.decode('hex'),
        P2P_PORT=23333,
        ADDRESS_VERSION=111,
        RPC_PORT=23332,
        RPC_CHECK=defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            'terracoinaddress' in (yield bitcoind.rpc_help()) and
            (yield bitcoind.rpc_getinfo())['testnet']
        )),
        SUBSIDY_FUNC=lambda height: 20*100000000 >> (height + 1)//1050000,
        POW_FUNC=data.hash256,
        BLOCK_PERIOD=120, # s
        SYMBOL='tTRC',
        CONF_FILE_FUNC=lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Terracoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Terracoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.terracoin'), 'terracoin.conf'),
        BLOCK_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/block/',
        ADDRESS_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/address/',
        TX_EXPLORER_URL_PREFIX='http://trc.cryptocoinexplorer.com/testnet/tx/',
        SANE_TARGET_RANGE=(2**256//2**32//1000 - 1, 2**256//2**32 - 1),
        DUMB_SCRYPT_DIFF=1,
        DUST_THRESHOLD=1e8,
    ),

)
for net_name, net in nets.iteritems():
    net.NAME = net_name
