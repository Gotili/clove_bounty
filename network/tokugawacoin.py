from clove.network.bitcoin import Bitcoin


class Tokugawa(Bitcoin):
    """
    Class with all the necessary Tokugawa network information based on
    https://github.com/TokugawaCoin/Tokugawa/blob/master/src/chainparams.cpp
    (date of access: 02/18/2018)
    """
    name = 'Tokugawa'
    symbols = ('TOK', )
    seeds = ("174.138.60.186",
             "138.197.150.224",
             "188.166.218.74")
    port = 21117
	
# no testnet