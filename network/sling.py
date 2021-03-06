from clove.network.bitcoin import Bitcoin


class Diamond(Bitcoin):
    """
    Class with all the necessary Diamond network information based on
    https://github.com/slingcoin/sling/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'sling'
    symbols = ('SLING', )
    seeds = ("slingseed1.slingcoin.io",
             "slingseed2.slingcoin.tech",
             "gseed3.sling.ws",
             "slingseed4.slingmarket.io",
             "slingseed5.slingmarket.tech",
             "slingseed6.slingcoin.info",
             "slingseed7.slingcoin.info")	
    port = 30137
	
# no testnet