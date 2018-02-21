from clove.network.bitcoin import Bitcoin


class SHACoin(Bitcoin):
    """
    Class with all the necessary SHACoin network information based on
    https://github.com/AltcoinsBeta/SHACoin-Dead/blob/master/src/net.cpp
    (date of access: 02/21/2018)
    """
    name = 'shacoin'
    symbols = ('SHA', )
    seeds = ("seed1.shacoin.us",
             "seed2.shacoin.us",
             "seed3.shacoin.us")
    port = 25555
	
