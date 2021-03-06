from clove.network.bitcoin import Bitcoin


class CannaCoin(Bitcoin):
    """
    Class with all the necessary CannaCoin network information based on
    https://github.com/Cannacoin-Project/Cannacoin/blob/Proof-of-Stake/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'cannacoin'
    symbols = ('CCN', )
    seeds = ("dnsseed.cannacoin.cc",
             "seed1.cannacoin.cc",
             "seed2.cannacoin.cc",
             "seed3.cannacoin.cc",
             "seed4.cannacoin.cc",
             "seed5.cannacoin.cc")
    port = 7143
	
   
class CannaCoinTestNet(CannaCoin):
    """
    Class with all the necessary CannaCoin testing network information based on
    https://github.com/Cannacoin-Project/Cannacoin/blob/Proof-of-Stake/src/net.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-cannacoin'
    seeds = ("testnet.cannacoin.cc")
    port = 17143               
	
