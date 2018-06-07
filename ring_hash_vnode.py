# -*- coding: utf-8 -*- 
from bisect import bisect_left
import util

class RingHashVNode:
    VNODES = 100
    def __init__(self, NODES):
        self.NODES = NODES
        self.ring = []
        self.hash2node = {}
        for n in xrange(NODES):
            for vn in xrange(self.VNODES):
                # 根据n和vn简单拼接得到新的独立k
                # 如n=88 vn=99，则拼接得到"0880000000099"
                k = str(n).zfill(3) + str(vn).zfill(10)
                h = util.hash(k)
                self.ring.append(h)
                self.hash2node[h] = n
        self.ring.sort()
        self.ringlen = len(self.ring)

    def get_node(self, data):
        h = util.hash(data)
        n = bisect_left(self.ring, h) % self.ringlen
        return self.hash2node[self.ring[n]]
