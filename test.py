# -*- coding: utf-8 -*- 
from normal_hash import NormalHash
from ring_hash import RingHash
from ring_hash_vnode import RingHashVNode 
from ring_hash_fixed_vnode import RingHashFixedVNode
import util

NODES1      = 100
NODES2      = 99
DATAS       = 10000000
DOWN_NODE_ID = 99

node_stat1 = [0 for i in xrange(NODES1)]
node_stat2 = [0 for i in xrange(NODES2)]
changes = 0

# TestNormalHash
# hash1 = NormalHash(NODES1)
# hash2 = NormalHash(NODES2)

# TestRingHash
hash1 = RingHash(NODES1)
hash2 = RingHash(NODES2)

# TestRingHashVNode
# hash1 = RingHashVNode(NODES1)
# hash2 = RingHashVNode(NODES2)

# TestRingHashFixedVNode
# hash1 = RingHashFixedVNode(NODES1)
# hash2 = RingHashFixedVNode(NODES1)
# hash2.node_down(DOWN_NODE_ID)
 
for data in xrange(DATAS):
    n1 = hash1.get_node(data)
    node_stat1[n1] += 1

    n2 = hash2.get_node(data)
    node_stat2[n2] += 1

    if n1 != n2:
        changes += 1

util.printNodeStats(DATAS, NODES1, node_stat1)
print("--- Node[" + str(DOWN_NODE_ID) + "] Down, Datas: "+ str(node_stat1[DOWN_NODE_ID]))
util.printNodeStats(DATAS, NODES2, node_stat2)
util.printChanges(DATAS, changes)