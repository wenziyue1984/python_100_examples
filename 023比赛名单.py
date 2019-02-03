# -*- coding:utf-8 -*-
__author__ = 'wenziyue'

'''
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。 
'''

def get_all():
	t1 = ['a', 'b', 'c']
	t2 = ['x', 'y', 'z']
	probably_list = []
	for i in t1:
		for j in t2:
			if i == 'a':
				if j != 'x':
					probably_list.append('{}-{}'.format(i, j))
					t2.remove(j)
					break
			elif i == 'c':
				if j in ['x', 'z']:
					pass
				else:
					probably_list.append('{}-{}'.format(i, j))
					t2.remove(j)
					break
			else:
				probably_list.append('{}-{}'.format(i, j))
				t2.remove(j)
				break
	print(probably_list)



'''
两个乒乓球队进行比赛，甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。
列出所有可能的对阵表，用dict形式，如：{a: x, b: y, c: z}
'''




'''
	i-0, i-1, i-2, i-3
i=0：0, -1, -2, -3
i=1：1, 0,  -1, -2
i=2：2, 1, 0, -1
i=3：3, 2, 1, 0
'''
def get_all_2():
	t1 = ['a', 'b', 'c']
	t2 = ['x', 'y', 'z']
	for i in t2:
		for j in t2:
			for k in t2:
				if i==j or i==k or j==k:
					continue
				print('a-{}, b-{}, c-{}'.format(i, j, k))



if __name__ == '__main__':
	# get_all()
	get_all_2()