# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
'''

def get_level(score):
	if isinstance(score, int) and score>=0 and score<=100:
		if score >= 90:
			print('A')
		elif 89 >= score >= 60:
			print('B')
		else:
			print('C')

if __name__=='__main__':
	get_level(9)