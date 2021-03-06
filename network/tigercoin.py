from clove.network.bitcoin import Bitcoin


class Tigercoin(Bitcoin):
    """
    Class with all the necessary Tigercoin network information based on
    https://github.com/TigerCoinDev/Tigercoin/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'tigercoin'
    symbols = ('TGC', )
    seeds = ("seed.bitcoin.sipa.be",
             "dnsseed.bluematt.me",
             "bitseed.xf2.org",
             "dnsseed.bitcoin.dashjr.org")
    port = 15660
	
# no testnet