# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，
低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
'''

def get_Royalty(profit):
	pro = pro_1 = pro_1_2 = pro_2_4 = pro_4_6 = pro_10 = 0
	if(profit-1000000>0):
		pro_10 = (profit-1000000)*0.01
		profit = 1000000
	if(profit-600000>0):
		pro_4_6 = (profit-600000)*0.015
		profit = 600000
	if(profit-400000>0):
		pro_2_4 = (profit-400000)*0.03
		profit = 400000
	if(profit-200000>0):
		pro_1_2 = (profit-200000)*0.05
		profit = 2000000
	if(profit-100000>0):
		pro_1 = (profit-100000)*0.075
		profit = 100000
	if(profit>0):
		pro = profit*0.1
	return pro+pro_1+pro_1_2+pro_2_4+pro_4_6+pro_10

if __name__=="__main__":
	print(get_Royalty(120000))