# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
打印出如下图案（菱形）

   *
  ***
 *****
*******
 *****
  ***
   *
'''

def print_lx():
	n = 0
	while n <= 4:
		print(' '*(4-n) + '*'*n + '*' + '*'*n)
		n += 1
	while n > 0:
		n -= 1
		print(' ' * (4 - n) + '*' * n + '*' + '*' * n)

if __name__ == '__main__':
	print_lx()