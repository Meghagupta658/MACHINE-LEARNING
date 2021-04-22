#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 17:03:04 2021

@author: meghagupta
"""

import pandas as pd 
import statsmodels.api as sm
dataset = pd.read_excel("Correlation.xlsx",sheet_name = 1)
Y = dataset.Attitude          #dependent varaible
X = dataset.Duration          #independent varaiable
X1 = sm.add_constant(X)       # adding constant which is require in linear regression
simple = sm.OLS(Y,X1)           #OLS is Ordinary Least Square Function for linear regression
                              # OLS(Y,X1) func of dependent and independent value
result = simple.fit()
result.summary()         #summary() for printing the summary                     


#Linear regression, also called Ordinary Least-Squares (OLS) Regression, is probably the most commonly used technique in Statistical Learning. 
#Ordinary Least Squares is the simplest and most common estimator in which the two (beta)s are chosen to minimize the square of the distance between the predicted values and the actual values. 
