# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
'''

def rev_print(s, l):
	if l == 0:
		return
	print(s[l-1])
	return rev_print(s, l-1)


if __name__ == '__main__':
	s = input('请输入5个字符：')
	l = len(s)
	rev_print(s, l)