#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:51:08 2021

@author: meghagupta
"""

import pandas as pd 

dataset = pd.read_excel("Bank_Personal_Loan_Modelling.xlsx", sheet_name =1)

dataset.columns

dataset1 = dataset.dropna()
dataset2 = dataset1.drop_duplicates()
dataset3 = dataset2.drop(['ID','ZIP Code'], axis = 1)

#Descriptive Analysis
dataset3[['Age', 'Experience', 'Income', 'Family', 'CCAvg',
       'Education', 'Mortgage',  'Securities Account',
       'CD Account', 'Online', 'CreditCard']].mean()

Bankloan_yes = dataset3[dataset3["Personal Loan"] == 1]
Bankloan_No = dataset3[dataset3['Personal Loan'] == 0]

Bank_yes = Bankloan_yes.describe()
Bank_no = Bankloan_No.describe()

import matplotlib.pyplot as plt 
plt.hist(dataset.Income)         #left side peakness so positive skewness mean more tha median

plt.hist(dataset.CCAvg)         #left side peakness so positive skewness mean more tha median

plt.hist(dataset.Age)           #Normally distributed as peak is on both side

plt.hist(dataset.Mortgage) 

plt.boxplot(dataset.Age)         # Normally distributed there is no outliers 

plt.boxplot(dataset.Income)      #There is outliers 

plt.boxplot(dataset.Mortgage)     #Positive skewness and there is number of outliers

plt.boxplot(dataset.CCAvg)

#Inferential Statistics
#For normally distributed data we can apply ttest
from scipy.stats import ttest_ind
stats,p = ttest_ind(Bankloan_yes.Age,Bankloan_No.Age)
print(stats,p)     #p value > 0.05 so accept null Hypothesis 

stats,p = ttest_ind(Bankloan_yes.Experience,Bankloan_No.Experience)
print(stats,p) 

stats,p = ttest_ind(Bankloan_yes.Income,Bankloan_No.Income)
print(stats,p)           #p value < 0.05 so reject null Hypothesis so there is significant difference in sancation of Loan with Average Income

#For non-normally distributed data we can apply Non-Parametric (MannWhitney Test)
#Non-Parametric : Population parameter is not used
#MannWhitneyu Test : when both 2 variables are independent of each other.

from scipy.stats import mannwhitneyu
stats,p = mannwhitneyu(Bankloan_yes.Mortgage,Bankloan_No.Mortgage)
print(stats,p)           #p value < 0.05 so reject null Hypothesis so there is significant difference in sancation of Loan with Mortgage

stats,p = mannwhitneyu(Bankloan_yes.CCAvg,Bankloan_No.CCAvg)
print(stats,p)  

#Chi Square Test : for checking the dependency of the variable
from scipy.stats import chi2_contingency
chitable = pd.crosstab(dataset3["Personal Loan"], dataset3["Education"])
stats,p,dof,expected = chi2_contingency(chitable)
print (stats,p)        #p value < 0.05 so reject null Hypothesis so there is significant difference in sancation of Loan and Education

chitable = pd.crosstab(dataset3["Personal Loan"], dataset3["Family"])
stats,p,dof,expected = chi2_contingency(chitable)
print (stats,p)        #p value < 0.05 so reject null Hypothesis so there is significant difference in sancation of Loan and Family

#Correlation : For finding relation between 2 variable
from scipy.stats import pearsonr
stats, p = pearsonr(dataset3["Personal Loan"], dataset3["Age"])
print(stats,p)       #Negatively correlated as stats value is negative and p value > 0.05 so accept null Hypothesis so there is no significant correlation b/t Personal Loan and Age

stats,p = pearsonr(dataset3["Personal Loan"],dataset3["Experience"])
print (stats,p)

stats,p = pearsonr(dataset3["Personal Loan"],dataset3["Income"])
print (stats,p)         #Positively correlated and p value < 0.05 so reject null Hypothesis so there is significant correlation b/t Personal Loan and Income

#Graph 
plt.plot(dataset3["Personal Loan"],dataset3["Income"])

correlation_matrix = dataset3.corr() 

#Logistic Regresstion : It is mainly used to find the causal effect relationship b/t the Dependent and Independent Variable in which DV should be Binary Categorical
import statsmodels.api as sm
Y = dataset3["Personal Loan"]
X = dataset3[['Age', 'Experience', 'Income', 'Family', 'CCAvg',
       'Education', 'Mortgage',  'Securities Account',
       'CD Account', 'Online', 'CreditCard']]
X1 = sm.add_constant(X)
Logistic = sm.Logit(Y,X1)
result=Logistic.fit()
result.summary()

