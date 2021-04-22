#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 09:21:39 2021

@author: meghagupta
"""

#code for House price effected by square feet, bedroom, bathroom, floors
#so there is  1 dependent variable (DV) and more independent variable(IDV)

#1. 1 dependent  varaible houseprice with 1 IDV square feet.
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("Linear Regression.xlsx", sheet_name =0)
dataset.head()
Y = dataset.price
X = dataset.sqft_living
X1 = sm.add_constant(X)
simple = sm.OLS(Y,X1)
result = simple.fit()
result.summary()

#R2 = 49.3%    49.3% of sq_feet effecting the house price.
# price = (-4.358e+04) + 280.6236(sqft_living)
#IDV is less than 0.05

#2. 1 dependent  varaible bedrooms with 1 IDV square feet.
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("Linear Regression.xlsx", sheet_name =0)
dataset.head()
Y = dataset.bedrooms
X = dataset.sqft_living
X1 = sm.add_constant(X)
simple = sm.OLS(Y,X1)
result = simple.fit()
result.summary()

#3. 1 dependent  varaible bathrooms with 1 IDV square feet.
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("Linear Regression.xlsx", sheet_name =0)
dataset.head()
Y = dataset.bathrooms 
X = dataset.sqft_living
X1 = sm.add_constant(X)
simple = sm.OLS(Y,X1)
result = simple.fit()
result.summary()

#4. 1 dependent  varaible floors with 1 IDV square feet.
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("Linear Regression.xlsx", sheet_name =0)
dataset.head()
Y = dataset.floors 
X = dataset.sqft_living
X1 = sm.add_constant(X)
simple = sm.OLS(Y,X1)
result = simple.fit()
result.summary()

#5. 1 dependent  varaible houseprice and other varaiable square feet, bathrooms, bedrooms and floors are independent variable.
import pandas as pd
import statsmodels.api as sm
dataset = pd.read_excel("Linear Regression.xlsx", sheet_name =0)
dataset.head()
Y = dataset.price
X = dataset[['sqft_living','bathrooms','bedrooms','floors']]
X1 = sm.add_constant(X)
multiple = sm.OLS(Y,X1)
result = multiple.fit()
result.summary()

#to create equation:
#House_price = 7.467e+04 + 309.3932(sqft_living) + 7853.5235(bathrooms) + (-5.785e+04)(bedrooms) + 200.4943(floors)
# P value of sqft_living,bathrooms,bedrooms is less than 0.05 so there is a causal relationship between IDV sqft_living,bathrooms,bedrooms and DV houseprice.
# P value of IDV floors is > o.o5 so it means Null hypothesis accepted and alternate hypothsis rejected.
#Change in IDV floors doesn't have causal effect on House Price.

#1.checking Hetroskedasticity pass.
import matplotlib.pyplot as plt
plt.hist(dataset.sqft_living)
plt.hist(dataset.bathrooms)
plt.hist(dataset.bedrooms)
plt.hist(dataset.floors)

#all grapshs are distritributed differently so Hetroskedasticity pass.



#2. Checking Autocorrelation
#code for finding correlation between 2 varaiables.
from scipy.stats import pearsonr
stats, p = pearsonr(dataset.price, dataset.sqft_living)
print(stats,p)       #output is 0.7020350524336835 0.0 so positively correlated.

stats, p = pearsonr(dataset.price, dataset.bathrooms)
print(stats,p)

stats, p = pearsonr(dataset.price, dataset.bedrooms)
print(stats,p)

stats, p = pearsonr(dataset.price, dataset.floors)
print(stats,p)

# all IDV are correlated with DV so aurocorrelation pass.

#3. Checking Multi-collinearity that will fail
dataset.corr()        #corr() is used to find the pairwise correlation of all columns in the dataframe.





