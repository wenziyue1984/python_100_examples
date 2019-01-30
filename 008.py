# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输出 9*9 乘法口诀表。
'''

def cfb():
	for i in range(1, 10):
		str_list = []
		for j in range(1, 10):
			if j <= i:
				# print('{} * {} = {}'.format(i, j, i*j))
				str_list.append('{} * {} = {}'.format(i, j, i*j))
		print(', '.join(str_list))

if __name__=='__main__':
	cfb()


# for i in range(1, 10):
#     print 
#     for j in range(1, i+1):
#         print "%d*%d=%d" % (i, j, i*j),