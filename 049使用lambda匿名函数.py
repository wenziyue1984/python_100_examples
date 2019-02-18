# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
使用lambda来创建匿名函数。
'''

if __name__ == '__main__':
	l = [1, 2, 3, 4, 5]
	l_new = map(lambda x: x**2, l)
	print(l_new)
	for i in l_new:
		print(i)

	l_new = filter(lambda x: x % 3 == 0, l)
	print(l_new)
	for i in l_new:
		print(i)

	maxnum = lambda x, y: (x > y) * x + (x < y) * y
	print('The largar one is {}'.format(maxnum(1, 2)))



'''
lambda x: x**2
就等于
def f(x):
	return x**2
冒号前面的是参数，后面的是操作逻辑

其实像上面的 map(lambda x: x**2, list) 我们也可以写成：[x**2 for i in list] 
在很多地方列表生成式都可以代替lambda

lambda x, y: (x > y) * x + (x < y) * y
(x>y)是一个布尔值，也可以参与运算，false是0，true是1
'''