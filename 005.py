# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
输入三个整数x,y,z，请把这三个数由小到大输出。
'''

def test(x, y, z):
	for i in sorted([x, y, z]):
		print(i)


if __name__=="__main__":
	num_str = input("请输入三个数字（a,b,c）:")
	num_list = num_str.split(",")
	test(int(num_list[0]), int(num_list[1]), int(num_list[2]))


'''
主要使用了sorted()函数排序，它是全局函数，返回一个有序的list，
也可以使用list.sort()来排序，但是这样原list将被改变
sorted()有可选参数reverse来控制升降序，默认reverse = False（升序）
sorted()也可以排序字符串，字典等一切可迭代对象
'''