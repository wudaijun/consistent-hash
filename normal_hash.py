# -*- coding: utf-8 -*- 
from bisect import bisect_left
import util

class NormalHash:
    def __init__(self, NODES):
        self.NODES = NODES

    def get_node(self, data):
        h = util.hash(data)
        return h % self.NODES

