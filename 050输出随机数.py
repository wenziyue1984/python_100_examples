# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输出一个随机数。
'''

import random

if __name__ == '__main__':
	print(random.random())
	print(random.randint(-10, 10))


'''
random.random()返回一个0-1的小数
random.randint(a, b)返回一个a-b之间的整数
'''