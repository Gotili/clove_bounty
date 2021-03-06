from clove.network.bitcoin import Bitcoin


class CreativeCoin(Bitcoin):
    """
    Class with all the necessary CreativeCoin (CREA) network information based on
    https://github.com/creativechain/creativechain-core/blob/master/src/chainparams.cpp
    (date of access: 02/17/2018)
    """
    name = 'creativecoin'
    symbols = ('CREA', )
    seeds = ('dnsseed.creativecoin.net', 'creaseed.owldevelopers.site')
    port = 10946


class CreativeCoinTestNet(CreativeCoin):
    """
    Class with all the necessary CreativeCoin (CREA) testing network information based on
    https://github.com/creativechain/creativechain-core/blob/master/src/chainparams.cpp    
    (date of access: 02/17/2018)
    """
    name = 'test-creativecoin'
    seeds = ('testnet-seed.creativecoin.net', 'tcreaseed.owldevelopers.site')
    port = 11946
