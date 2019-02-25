# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
列表排序及连接。
'''

if __name__ == '__main__':
	a = [2, 3, 5, 1, 4]
	b = [6, 7, 8, 9, 10]
	# 排序
	a.sort()
	print(a)
	# 连接
	d = a + b
	print(d)
	a.extend(b)
	print(a)