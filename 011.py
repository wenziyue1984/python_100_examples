# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月起每个月又生一对兔子，假如兔子都不死，
问每个月的兔子总数为多少？ 
'''

# import sys
# sys.setrecursionlimit(100000)

def get_num(mouth):
	m = 0
	adult = 0
	child = [0]
	while m <= mouth:
		# 未成年兔子都大了一月
		child = [x+1 for x in child]
		# 算出多少兔子成年了
		c_to_a = len([x for x in child if x == 2])
		# 在list里删除所有等于2的值
		child = [x for x in child if x != 2]
		# 给list里添加新生的兔子
		child.extend([0 for _ in range(adult)])
		# 将成年的兔子加到adult里
		adult += c_to_a
		m += 1
	# print('adult:{}'.format(adult))
	# print('child:{}'.format(child))
	return len(child)+adult

def get_num_2(mouth):
	if mouth == 1:
		return 1
	if mouth == 2:
		return 1
	if mouth == 3:
		return 2
	return get_num_2(mouth-1) + get_num_2(mouth-3)

if __name__=='__main__':
	print([get_num(x) for x in range(10)])
	# print([get_num_2(x) for x in range(10)])
	print(get_num_2(10))
	# print('兔子总数：{}'.format(get_num(10)))