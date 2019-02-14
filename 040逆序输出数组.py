# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
将一个数组逆序输出。
'''

from random import randint

def test(l):
	print(l)
	l.sort()
	print(l)
	for i in l[::-1]:
		print(i)


if __name__ == '__main__':
	test([randint(1, 100) for _ in range(5)])