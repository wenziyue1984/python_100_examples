# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
求100之内的素数。
素数，指在大于1的自然数中，除了1和该数自身外，无法被其他自然数整除的数
'''

def test(num):
	num_list = [x for x in range(2, num+1)]
	for i in range(2, num+1):
		for j in range(2, i):
			if i % j == 0:
				num_list.remove(i)
				break
	print(num_list, len(num_list))

'''答案的方法'''
def test2(n):
	num_list = []
	for num in range(2, n + 1):
		# 素数大于 1
		if num > 1:
			for i in range(2, num):
				if (num % i) == 0:
					break
			else:
				num_list.append(num)
	print(num_list, len(num_list))

if __name__ == '__main__':
	# test(100)
	# test2(100)
	for i in range(3):
		if i<4:
			break
	else:
		print(1)


'''
答案的方法比我的更好，用了for...break...else，这个我以前都没用过，会更方便
在for循环完整完成后才执行else；如果中途从break跳出，则连else一起跳出。
	for i in range(3):
		if i>4:
			break
	else:
		print(1)
	# for循环内没有执行break，所有for循环完毕后会执行else内的代码
	
	for i in range(3):
		if i<4:
			break
	else:
		print(1)
	# for循环内会执行break，会直接跳出for循环，顺带着也会跳出else，所以print’不会执行
	
使用for...break...else会更好的解决像这道题的情况
'''