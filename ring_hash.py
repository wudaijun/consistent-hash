# -*- coding: utf-8 -*- 
from bisect import bisect_left
import util

class RingHash:
    def __init__(self, NODES):
        self.NODES = NODES
        self.ring = []
        self.hash2node = {}
        for n in xrange(NODES):
            h = util.hash(n)
            self.ring.append(h)
            self.hash2node[h] = n
        self.ring.sort()

    def get_node(self, data):
        h = util.hash(data)
        n = bisect_left(self.ring, h) % self.NODES
        return self.hash2node[self.ring[n]]
