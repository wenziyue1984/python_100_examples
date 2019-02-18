# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
数字比较。
'''

def compare(a, b):
	# 判读参数是否为int或者float
	if not ((isinstance(a, int) or isinstance(a, float)) and (isinstance(b, int) or isinstance(b, float))):
		exit('参数格式有误...')
	if a > b:
		print('{}大于{}'.format(a, b))
	elif a == b:
		print('{}等于{}'.format(a, b))
	else:
		print('{}小于{}'.format(a, b))


if __name__ == '__main__':
	compare(1.2, 2.0)