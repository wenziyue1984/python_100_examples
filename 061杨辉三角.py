# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
打印出杨辉三角形（要求打印出10行如下图）。
1 
1 1 
1 2 1 
1 3 3 1 
1 4 6 4 1 
1 5 10 10 5 1 
1 6 15 20 15 6 1 
1 7 21 35 35 21 7 1 
1 8 28 56 70 56 28 8 1 
1 9 36 84 126 126 84 36 9 1
'''

def test(n):
	yh_list = []
	for i in range(n):
		index_list = []
		if i == 0:
			pass
		else:
			for j in range(i):
				if j == 0:
					index_list.append(1)
				else:
					index_list.append(yh_list[i-1][j-1] + yh_list[i-1][j])
		index_list.append(1)
		yh_list.append(index_list)
	return yh_list


if __name__ == '__main__':
	yh = test(10)
	for i in yh:
		print(i)


'''
杨辉三角：
每行头尾都是1
除了头尾每个数都等于上面两个数之和
'''