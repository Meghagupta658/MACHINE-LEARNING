#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 00:48:37 2021

@author: meghagupta
"""

import pandas as pd 
import numpy as np 
from sklearn import tree

dataset = pd.read_csv("Attrition Rate Analysis.csv")

dataset.columns

dataset = dataset.dropna()
dataset = dataset.drop_duplicates()

from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()
dataset["Attrition"]=label_encoder.fit_transform(dataset["Attrition"])

tree_model= tree.DecisionTreeClassifier()
tree_model.fit( X=pd.DataFrame(dataset["MonthlyIncome"]) , y=dataset["Attrition"])

with open("ARA.dot",'w') as f:
    f = tree.export_graphviz(tree_model,feature_names=["MonthlyIncome"],out_file=f);
