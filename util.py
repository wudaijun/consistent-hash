from hashlib import md5
from struct import unpack_from

def printNodeStats(DATAS, NODES, node_stat):
	_ave = DATAS / NODES
	_max = max(node_stat)
	_min = min(node_stat)
	print("Ave: %d" % _ave)
	print("Max: %d\t(%0.2f%%)" % (_max, (_max - _ave) * 100.0 / _ave))
	print("Min: %d\t(%0.2f%%)" % (_min, (_ave - _min) * 100.0 / _ave))

def printChanges(DATAS, changes):
	print("Change: %d\t(%0.2f%%)" % (changes, changes * 100.0 / DATAS))	

def hash(value):
    k = md5(str(value)).digest()
    ha = unpack_from(">I", k)[0]
    return ha

