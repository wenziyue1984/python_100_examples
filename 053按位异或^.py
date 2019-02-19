# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
学习使用按位异或 ^
'''

if __name__ == '__main__':
	a = 2
	b = a ^ 5
	print('a ^ 5 = {}'.format(b))
	b ^= 7
	print('b ^ 7 = {}'.format(b))

'''
按位异或

对位相加,特别要注意的是不进位.

2 ^ 5 = 010 ^ 101 = 111 = 7
7 ^ 7 = 111 ^ 111 = 000 = 0
'''