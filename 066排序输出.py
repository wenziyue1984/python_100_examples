# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输入3个数a,b,c，按大小顺序输出。　
'''


def zidong_paixu(l):
	l_copy = l.copy()
	l_copy.sort()
	print(l_copy)

def shoudong_paixu(l):
	l_copy = l.copy()
	for i in range(1, len(l_copy)):
		for j in range(len(l_copy)-i):
			if l_copy[j] > l_copy[j+1]:
				index = l_copy[j]
				l_copy[j] = l_copy[j+1]
				l_copy[j+1] = index
	print(l_copy)

if __name__ == '__main__':
	s1 = input('请输出第一个数：')
	s2 = input('请输出第二个数：')
	s3 = input('请输出第三个数：')
	# l = [s1, s2, s3]
	l = [int(s1), int(s2), int(s3)]
	zidong_paixu(l)
	shoudong_paixu(l)
	print(l)