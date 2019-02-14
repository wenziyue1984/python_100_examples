# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
'''

import random

# 简单版，数组l中都是数字，按从小到大已排好序
def test(l, num):
	if isinstance(l, list) and isinstance(num, int or float):
		l.append(num)
		l.sort()
		return l

# 复杂版，数组l中都是数字，按从小到大已排好序，自己写数字比较方法
def test2(l, num):
	if isinstance(l, list) and isinstance(num, int or float):
		if num < l[0]:
			l[:0] = [num]
			return l
		if num > l[len(l)-1]:
			l.append(num)
			return l
		for i in range(len(l)-1):
			if num > l[i] and num < l[i+1]:
				l[i+1:i+1] = [num]
				return l


if __name__ == '__main__':
	l = [random.randint(1, 100) for _ in range(5)]
	l.sort()
	num = random.randint(1, 100)
	print(l, num)
	# l_new = test(l, num)
	l_new = test2(l, num)
	print(l_new)

