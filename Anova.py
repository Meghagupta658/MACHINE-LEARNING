#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:07:01 2021

@author: meghagupta
"""

# Anova code 1 IDV categorical and 1 DV continuous
import pandas as pd 
import statsmodels.api as sm
dataset = pd.read_excel("ANCOVA1.xlsx",sheet_name = 0)

from statsmodels.formula.api import ols
model = ols("Sales~C(Promotion)",dataset).fit()   #sales is DV and Promotion is IDV
oneway = sm.stats.anova_lm(model,type=2)           #anova_lm anova linear model  #type = 2 when anova and ancova and 1 when regression , 3 when discriminant analysis
print(oneway)

#2 way anova
model = ols("Sales~C(Promotion)+C(Coupon)",dataset).fit()   #sales is DV and Promotion, Coupons is IDV
twoway = sm.stats.anova_lm(model,type=2)   
print(twoway)  
     
#Ancova:  IDV is categorical and continuous and 1 DV continuous
model = ols("Sales~C(Promotion)+C(Coupon)+ClietelRatings",dataset).fit()   #sales is DV and (Promotion, Coupons )categaorical and client Rating(continuous) is IDV 
ancova = sm.stats.anova_lm(model,type=2)   
print(ancova)


#eta:

def anova_table(oneway):
    oneway['eta_sq'] = oneway[:-1]['sum_sq']/sum(oneway['sum_sq'])
    cols = ['df','sum_sq','mean_sq','F','PR(>F)','eta_sq']
    oneway = oneway[cols]
    return oneway

anova_table(oneway)
anova_table(twoway)
anova_table(ancova)