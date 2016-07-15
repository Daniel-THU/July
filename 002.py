# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 13:23:03 2016

@author: liulei
"""

# 嵌套的字典 给电影打分   

# 嵌套字典的获取， 类似矩阵 二维数组

critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}



# 欧几里得距离返回相关度  1表示相同偏好  

from math import sqrt

# prefs表示嵌套的打分字典， person表示人
def sim_distance(prefs, person1, person2):
    si = {}
    sum_of_squares=0

    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
            sum_of_squares += pow(prefs[person1][item]-prefs[person2][item],2)
    if len(si) == 0:
        return 0
    else:
        return 1/(1+sqrt(sum_of_squares))
    
#测试
#print sim_distance(critics, 'Lisa Rose', 'Gene Seymour')


#皮尔逊相关系数

# 有问题 就是交集为0的时候 应该先判断  这样 for循环需要写两次
# 交集不为空的时候  正常运行
def sim_pearson(prefs, person1, person2):
    si = {}
#    sum_of_squares=0
    sum1, sum2 =0,0
    sum1Sq,sum2Sq , pSum=0,0,0
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
            sum1 += prefs[person1][item]
            sum2 += prefs[person2][item]
            
            sum1Sq += pow(prefs[person1][item],2)
            sum2Sq += pow(prefs[person2][item],2)
            
            pSum += prefs[person1][item]* prefs[person2][item]
    if len(si)==0:
        return 0
    else:
        num = pSum - (sum1*sum2/len(si))
        den = sqrt((sum1Sq - pow(sum1, 2)/len(si))*(sum2Sq - pow(sum2,2)/len(si)))
        
        if den ==0:
            return 0
        r=num/den
        
        return r
    

# 题目继续拓展  输入的任一人名， 输出其他人跟他的近似度列表,同时输出 相似度和人名
def topMatches(prefs, person, n=5, similarity = sim_pearson):
    scores = [(similarity(prefs, person, other),other) for other in prefs if other != person]
    
    scores.sort()
    scores.reverse()
    return scores[0:n]
    
#以上我们寻找的是跟我们的电影相同偏好的人
#现在我们需要给自己寻找总体打分比较高的电影,不在自己的列表 但在别人的列表
'''
优雅的代码
多看几遍
'''
def getRecommendations(prefs, person, similarity = sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        if other == person:
            continue
        sim = similarity(prefs, person, other)
        if sim <= 0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                #相似度*评价值
                totals[item] += prefs[other][item]*sim
                
                #相似度之和
                simSums.setdefault(item,0)
                simSums[item] += sim


    rankings = [(total/simSums[item],item) for item ,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    
    return rankings


'''
换一个维度
看物品的相似度
然后推荐
'''
def transformPrefs(prefs):
    result={}
    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})
            result[item][person] = prefs[person][item]
    return result

# 构造物品比较数据集
def calculateSimilarItems(prefs, n=10):
    result = {}
    itemPrefs = transformPrefs(prefs)
    for item in itemPrefs:     
        scores = topMatches(itemPrefs, item, n=n, similarity= sim_distance)
        result[item] = scores
    
    return result

#print calculateSimilarItems(critics)

#def getRecommendedItems(prefs, itemMatch, user):
#    userRatings = prefs[user]
#    scores={}
#    totalSim={}
#    
#    for (item, rating) in userRatings.items():
#        pass
#


def loadMovieLens(path='/Users/liulei/Desktop/python这周看完之前的代码/Programming collective intelligence/ml'):
    movies={}
    for line in open(path +'/u.item'):
        (id, title) = line.split('|')[0:2]
        movies[id]=title
    
    
    prefs={}
    for line in open(path+'/u.data'):
        (user,movieid,rating,ts)=line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movieid]]=float(rating)
    return prefs
    
prefs=  loadMovieLens()
print prefs['87']
    