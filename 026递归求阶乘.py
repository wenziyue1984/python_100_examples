# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
利用递归方法求5!
'''

def get_num(n):
	if n == 1:
		return 1
	return n*get_num(n-1)

if __name__ == '__main__':
	print(get_num(5))