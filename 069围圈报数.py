# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
'''

def test(l, n=1):
	if len(l) > 1:
		l_remove = []
		for i in range(len(l)):
			if (i+n) % 3 == 0:
				l_remove.append(l[i])
			if i == len(l)-1:
				n = (i+n) % 3
		l_new = [x for x in l if x not in l_remove]
		test(l_new, n+1)
	else:
		print(l)


if __name__ == '__main__':
	l = [x for x in range(1, 35)]
	test(l)

'''
递归求解，有很多的小细节需要注意
'''