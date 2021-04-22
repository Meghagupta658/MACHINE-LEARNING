#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 13:08:13 2021

@author: meghagupta
"""

import pandas as pd 
import numpy as np 
from sklearn import tree

dataset = pd.read_excel("Bank_Personal_Loan_Modelling.xlsx", sheet_name = 1)

dataset.columns

dataset = dataset.dropna()
dataset = dataset.drop_duplicates()

tree_model= tree.DecisionTreeClassifier()
tree_model.fit( X=pd.DataFrame(dataset["Income"]) , y=dataset["Personal Loan"])

with open("BPLM1.dot",'w') as f:
    f = tree.export_graphviz(tree_model,feature_names=["Income"],out_file=f);

#for finding important independent varaiable from number of varaibles from dataset Random Forest is applied
from sklearn.ensemble import RandomForestClassifier
rf_model =RandomForestClassifier(n_estimators = 1000, max_features = 2, oob_score = True)
features = ['Age', 'Experience', 'Income', 'Family', 'CCAvg',
       'Education', 'Mortgage', 'Securities Account',
       'CD Account', 'Online', 'CreditCard']
rf_model.fit(X=dataset[features], y=dataset["Personal Loan"])
print("OOB Accuracy")
print(rf_model.oob_score_)   #rf_model.oob_score  it will give true false value and rf_model.oob_score_ will give point percentage value

for feature,imp in zip(features,rf_model.feature_importances_):
    print(feature,imp);
    
predictors = pd.DataFrame([dataset["Income"],dataset["CCAvg"],dataset["Education"]]).T
tree_model= tree.DecisionTreeClassifier(max_depth=6)    # for defining tree length
tree_model.fit(X= predictors,y=dataset["Personal Loan"])

with open("BPLM2.dot",'w') as f:
    f = tree.export_graphviz(tree_model,feature_names=["Income","CCAvg","Education"],out_file=f);