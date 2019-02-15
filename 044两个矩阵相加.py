# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵
'''


'''
[1,2,3]
[4,5,6]
[7,8,9]

[]
'''
def add_jz(l1, l2):
	l_new = []
	for i in range(3):
		l = []
		for j in range(3):
			l.append(l1[i][j] + l2[i][j])
		l_new.append(l)
	print(l_new)


if __name__ == '__main__':
	l1 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	l2 = [[1, 1, 1], [1, 1, 1], [1, 1, 2]]
	add_jz(l1, l2)