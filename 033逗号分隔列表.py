# -*- coding:utf-8 -*-
__author__ = 'wenziyue'


'''
按逗号分隔列表。
'''

def test(l):
	s = ','.join([str(n) for n in l])
	return s


if __name__ == '__main__':
	print(test([1, 2, 3]))