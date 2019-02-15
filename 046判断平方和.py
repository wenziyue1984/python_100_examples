# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求输入数字的平方，如果平方运算后小于 50 则退出。
'''

import math

def test():
	while True:
		num = float(input('请输入数字：'))
		sq = num**2
		if sq < 50:
			print('exit')
			exit()
		print('平方是：{}'.format(sq))


if __name__ == '__main__':
	test()