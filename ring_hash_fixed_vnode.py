# -*- coding: utf-8 -*- 
from bisect import bisect_left
import util

class RingHashFixedVNode:
    VNODES  = 10000 # 将整个环分为VNODES份
    def __init__(self, NODES):
        self.NODES = NODES
        self.ring = [] # 下标为VNode 值为对应的Node
        for vn in xrange(self.VNODES):
            self.ring.append(vn%NODES)

    def get_node(self, data):
        h = util.hash(data)
        vn = h%self.VNODES
        return self.ring[vn]

    # 某个节点挂掉了，将其数据手动均匀分到其它节点上
    def node_down(self, n):
        self.NODES -= 1
        for vn in xrange(self.VNODES):
            if self.ring[vn] == n:
                self.ring[vn] = vn % self.NODES
