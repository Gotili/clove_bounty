from clove.network.bitcoin import Bitcoin


class Mbitbooks(Bitcoin):
    """
    Class with all the necessary Mbitbooks network information based on
    https://github.com/mbitbooks/Mbitbooks/blob/master/src/net.cpp
    (date of access: 02/16/2018)
    """
    name = 'mbitbooks'
    symbols = ('MBIT', )
    seeds = ("59.95.128.24",
             "95.211.57.108.")
    port = 12207
