# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
反向输出一个链表。
'''

if __name__ == '__main__':
	l = []
	for i in range(10):
		l.append(i)
	for j in l[::-1]:
		print(j)
	print('*'*30)
	l.reverse()
	for k in l:
		print(k)