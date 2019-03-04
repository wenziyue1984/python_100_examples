# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
时间函数举例2
'''

import time

if __name__ == '__main__':
	start = time.time()
	for i in range(3000):
		print(i)
	end = time.time()
	print(end - start)


'''
利用时间戳计算函数运行时间
'''