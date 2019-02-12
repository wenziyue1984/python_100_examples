# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
按相反的顺序输出列表的值。
'''


def print_rev(l):
	l_rev = []
	for i in range(1, len(l)+1):
		l_rev.append(l[len(l)-i])
	for i in l_rev:
		print(i)

'''答案方法，直接利用list[::-1]'''
def test(l):
	for i in l[::-1]:
		print(i)

if __name__ == '__main__':
	l = [1, 2, 3]
	# print_rev(l)
	test(l)


'''
复习了list切片，利用这个特性生成了逆序list
'''