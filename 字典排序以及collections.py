# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 16:16:25 2016

@author: liulei
"""
'''
字典是无序的 
如何有序的打印输出
'''

dic = {'a':31, 'bc':5, 'c':3, 'asd':4, 'aa':74, 'd':0}

#变成一个列表  不再是字典
dic = sorted(dic.items(), key = lambda d : d[1])


print dic

import collections

string = ('puppy', 'kitten', 'puppy','kitten','puppy')
count = collections.defaultdict(lambda:0)

for s in string:
    count[s]+=1

#print count.items()



