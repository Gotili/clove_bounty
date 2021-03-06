from clove.network.bitcoin import Bitcoin


class Crown(Bitcoin):
    """
    Class with all the necessary Crown network information based on
    https://github.com/Crowndev/crowncoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'crown'
    symbols = ('CRW', )
    seeds = (
        'fra-crwdns.infernopool.com',
        'blr-crwdns.infernopool.com',
        'sgp-crwdns.infernopool.com',
        'lon-crwdns.infernopool.com',
        'nyc-crwdns.infernopool.com',
        'tor-crwdns.infernopool.com',
        'sfo-crwdns.infernopool.com',
        'ams-crwdns.infernopool.com',
        'crw.infernopool.com',
    )
    port = 9340


class CrownTestNet(Crown):
    """
    Class with all the necessary Crown testnet information based on
    https://github.com/Crowndev/crowncoin/blob/master/src/chainparams.cpp
    (date of access: 02/14/2018)
    """
    name = 'test-crown'
    seeds = (
        'fra-testnet-crwdns.infernopool.com',
        'sgp-testnet-crwdns.infernopool.com',
        'lon-testnet-crwdns.infernopool.com',
        'nyc-testnet-crwdns.infernopool.com',
        'tor-testnet-crwdns.infernopool.com',
        'sfo-testnet-crwdns.infernopool.com',
        'ams-testnet-crwdns.infernopool.com,
        'crw-testnet.infernopool.com',
    )
    port = 19340
