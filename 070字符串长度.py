# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度。
'''

def test(s):
	return len(s)


if __name__ == '__main__':
	s = input('请输入字符串：')
	print('字符串长度为：{}'.format(test(s)))