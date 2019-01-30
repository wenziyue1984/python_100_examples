# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
判断101-200之间有多少个素数，并输出所有素数。
素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数
'''

def get_num(small, big):
	num_list = [x for x in range(small, big)]
	for i in range(small, big):
		for num in range(2, i):
			if i % num == 0:
				num_list.remove(i)
				break
	print(num_list)
	print('{}-{}之间素数个数为：{}'.format(small, big, len(num_list)))
	# return num_list

if __name__=='__main__':
	get_num(101, 200)
	get_num(0, 100)