# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
学习使用按位与 & 。
'''

if __name__ == '__main__':
	b = 3 & 5
	print('3 & 5 = {}'.format(b))
	c = -1 & -2
	print('-1 & -2 = {}'.format(c))
	d = -2 & 6
	print('-2 & 6 = {}'.format(d))


'''
吸尘器，扫地机器人，ipad，植发，猫，球鞋，mac，吉他，
1500 + 2500 + 2000 + 15000 + 2000 + 1000 + 10000 + 1000

二进制 按位运算

1&1=1，1&0=0，0&0=0

3 & 5
3的二进制补码是 11,  5的是101, 3&5也就是011&101,先看百位(其实不是百位,这样做只是便于理解) 一个0一个1,
根据(1&1=1，1&0=0，0&0=0)可知百位应该是0,同样十位上的数字1&0=0,个位上的数字1&1=1,因此最后的结果是1.
(这之后本来应该还有一步,因为我们现在得到的数值只是所求答案的补码,但是因为正数的补码即是它本身,所以就省略了。
不过,如果是负数参与按位运算就不能省略最后这一步了).

-1 & -2	(负数和负数按位与运算的结果要从补码转成原码)
解法:-1的补码是11111111,  -2的补码是11111110, 
11111111 & 11111110 = 11111110,这个是补码,
再转化位原码为100000010 (负数转换位原码的方法是减一取反),最后转换为十进制是 -2

-2 & 6   
解法:-2的补码是11111110,  6的补码是00000110,   
11111110 & 00000110 = 00000110,转为原码为:110,转化位十进制就是6.
'''