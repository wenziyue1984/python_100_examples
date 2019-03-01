# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：
每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
'''

def test(n):
	if isinstance(n, int) and 1000 <= n <= 9999:
		# a = int(str(n)[0])
		# b = int(str(n)[1])
		# c = int(str(n)[2])
		# d = int(str(n)[3])
		n_list = [int(i) for i in str(n)]
		print(n_list)
		n_new = []
		for i in n_list:
			n_new.append((i+5) % 10)
		n_new.reverse()
		result = ''.join((map(lambda x: str(x), n_new)))
		print(result)


if __name__ == '__main__':
	test(1234)