#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 15:22:27 2021

@author: meghagupta
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

dataset = pd.read_csv("SVMtrain.csv")
dataset.columns

le = preprocessing.LabelEncoder()
le.fit(dataset['Sex'])
print(le.classes_)
dataset['Sex'] = le.transform(dataset['Sex'])

dataset1 = dataset.drop(['PassengerId'],axis =1)
y = dataset1['Survived']
x = dataset1.drop(['Survived'],axis=1)

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.3, random_state = True)
x_train.head()
x_test.head()
y_train.head()
y_test.head()

from sklearn.naive_bayes import *
clf = BernoulliNB()

y_pred = clf.fit(x_train,y_train).predict(x_test)      #fit()The fit() method takes the training data as arguments, which can be one array in the case of unsupervised learning, or two arrays in the case of supervised learning. Note that the model is fitted using X and y , but the object holds no reference to X and y .

accuracy_score(y_test,y_pred,normalize = True)

confusion_matrix(y_test,y_pred)