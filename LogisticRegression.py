#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Created on Sun Mar 14 11:34:04 2021

@author: meghagupta
"""

#Logistic Regression
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("2 Logistic Regression.xlsx", sheet_name = 0)
Y = dataset.Admit
X = dataset[['GRE','GPA','Rank']]
X1 = sm.add_constant(X)
Logistic = sm.Logit(Y,X1)    #n statistics, the logistic model (or logit model) is used to model the probability of a certain class or event existing such as pass/fail
result = Logistic.fit()
result.summary()

#The logit link function is used to model the probability of 'success' as a function of covariates (e.g., logistic regression).