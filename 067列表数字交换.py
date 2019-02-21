# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
'''

def test(l):
	# 找到最大的数字，与头交换
	num_max = l[0]
	index_max = 0
	for i in range(len(l)):
		if l[i] > num_max:
			# num_max = l[i]
			index_max = i
	num_max = l[0]
	l[0] = l[index_max]
	l[index_max] = num_max

	# 找到最小的数字，与尾交换
	num_min = l[0]
	index_min = 0
	for i in range(1, len(l)):
		if l[i] < num_min:
			num_min = l[i]
			index_min = i
	num_min = l[-1]
	l[-1] = l[index_min]
	l[index_min] = num_min