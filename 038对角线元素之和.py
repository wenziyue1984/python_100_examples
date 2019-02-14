# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求一个3*3矩阵主对角线元素之和。
'''

def test(a, b, c):
	sum = 0
	l = [a, b, c]
	for i in range(3):
		sum += l[i][i]
	print(sum)


if __name__ == '__main__':
	test([1, 2, 3], [4, 5, 6], [7, 8, 9])