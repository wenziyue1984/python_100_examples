# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求0—7所能组成的奇数个数。

组成1位数是4个。
组成2位数是7*4个。
组成3位数是7*8*4个。
组成4位数是7*8*8*4个。
...
组成8位数是7*8*8*8*8*8*8*4个。

从二位数开始，7* 8**i *4
'''

if __name__ == '__main__':
	s = 4
	for i in range(7):
		s += 7 * 4 * 8**i
	print(s)


	# 以下为答案的方法，看不太懂
	# sum = 4
    # s = 4
    # for j in range(2,9):
    #     print(sum)
    #     if j <= 2:
    #         s *= 7
    #     else:
    #         s *= 8
    #     sum += s
    # print('sum = %d' % sum)