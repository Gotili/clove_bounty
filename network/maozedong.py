from clove.network.bitcoin import Bitcoin


class MaoZedong(Bitcoin):
    """
    Class with all the necessary MaoZedong network information based on
    https://github.com/mao-zedongx/mao-zedong/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'maozedong'
    symbols = ('MAO', )
    seeds = ("45.76.47.47",
             "explorer.mao-zedong.net",
             "node1.mao-zedong.net",
             "node2.mao-zedong.net",
             "node3.mao-zedong.net",
             "node4.mao-zedong.net",
             "node5.mao-zedong.net",
             "node6.mao-zedong.net",
             "node7.mao-zedong.net",
             "dnsseed.mao-zedong.net",
             "dnsseed1.mao-zedong.net",
             "dnsseed2.mao-zedong.net",
             "dnsseed3.mao-zedong.net",
             "dnsseed4.mao-zedong.net",
             "dnsseed5.mao-zedong.net")
    port = 9670


# Has no testnet
