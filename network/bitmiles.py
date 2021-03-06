from clove.network.bitcoin import Bitcoin


class Bitmiles(Bitcoin):
    """
    Class with all the necessary Bitmiles network information based on
    https://github.com/rynaldos/bitmiles-source/blob/master/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'bitmiles'
    symbols = ('BTMI', )
    seeds =  ("95.85.60.246")
    port = 29156
	
# Has no testnet