# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 13:22:08 2016

@author: liulei
"""

import numpy as np
from sklearn import svm
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt

data   = []
labels = []
with open("/Users/liulei/Desktop/data1.txt") as ifile:
        for line in ifile:
            tokens = line.strip().split(' ')
            data.append([float(tk) for tk in tokens[:-1]])
            labels.append(tokens[-1])
x = np.array(data)
labels = np.array(labels)
y = np.zeros(labels.shape)
y[labels=='fat']=1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2)

clf_linear  = svm.SVC(kernel='linear').fit(x, y)
clf_poly    = svm.SVC(kernel='poly', degree=3).fit(x, y)
clf_rbf     = svm.SVC().fit(x, y)
clf_sigmoid = svm.SVC(kernel='sigmoid').fit(x, y)

for i, clf in enumerate((clf_linear, clf_poly, clf_rbf, clf_sigmoid)):
    answer = clf_linear.predict(x_test)
    print(np.mean( answer == y_test))