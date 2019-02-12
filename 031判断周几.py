# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
'''

def judge_week():
	letter = input("please input:")
	# while letter  != 'Y':
	if letter.upper() == 'S':
		print('please input second letter:')
		letter = input("please input:")
		if letter.lower() == 'a':
			print('Saturday')
		elif letter.lower() == 'u':
			print('Sunday')
		else:
			print('data error')
	elif letter.upper() == 'F':
		print('Friday')
	elif letter.upper() == 'M':
		print('Monday')
	elif letter.upper() == 'T':
		print('please input second letter')
		letter = input("please input:")
		if letter.lower() == 'u':
			print('Tuesday')
		elif letter.lower() == 'h':
			print('Thursday')
		else:
			print('data error')
	elif letter.upper() == 'W':
		print('Wednesday')
	else:
		print('data error')


if __name__ == '__main__':
	judge_week()


'''
练习了一下大小写转换
str.upper() 转大写
str.lower() 转小写
str.capitalize() 第一个字母大写
str.title() 把一段话里每一个单词的第一个字母大写
'''