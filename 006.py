# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
斐波那契数列。
斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……
'''


def fb(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n >= 2:
		return fb(n-1)+fb(n-2)

if __name__=="__main__":
	fb_list = []
	for i in range(20):
		fb_list.append(fb(i))
	print(fb_list)


'''
还可以用迭代器实现
'''