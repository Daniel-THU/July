# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 13:56:31 2016

@author: liulei
"""
'''

任一英文文本文件 统计其中单词出现个数
用到正则

'''

import re

def  countWords():
    with open('text.txt','r') as file:
        data = file.read()
        
    words = re.compile(r'([a-zA-Z]+)')
    
    
    
    #统计
    dic ={}
    for i in words.findall(data):
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    
    
    numlist = []
    
    for word , count in dic.items():
        numlist.append((word, count))   # 元组
        
    
    # 排序
    numlist.sort(key = lambda t : t[1])
    
    #输出
    for i in numlist:
        print (i[0], i[1])
#test        
#if __name__ == '__main__':
#    countWords()


