# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
对10个数进行排序。
'''

import random

def maopao(l):
	l_new = l
	for i in range(1, len(l)):
		for j in range(len(l)-i):
			if l[j] > l[j+1]:
				a = l[j]
				l[j] = l[j+1]
				l[j+1] = a
	return l_new


if __name__ == '__main__':
	l = [random.randint(1, 100) for _ in range(10)]
	print(l)
	l_sort = maopao(l)
	print(l_sort)
	# 更简单的方法直接list.sort()
	l.sort()
	print(l)


'''
list.sort()会改变原list
'''

