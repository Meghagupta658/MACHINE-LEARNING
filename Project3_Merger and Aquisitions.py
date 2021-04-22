#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 19:48:57 2021

@author: meghagupta
"""

import pandas as pd
dataset = pd.read_excel("1. Services.xlsx",sheet_name=0)
dataset.head()

#same company 2 different situation so paired sample so 2 sample paired ttest is applied
from scipy.stats import ttest_rel
stats,p = ttest_rel(dataset.PreMerger,dataset.PostMerger)
print(stats,p)    #p value < 0.05 so reject null hypothesis so there is significant difference in airtel stock return b/t premerger and postmerger

#Factor analysis for finding important IDV 
dataset1 = pd.read_excel("Post Merger Aquisition.xlsx",sheet_name = 6)

from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
dataset1= dataset1.dropna()
X= dataset1.values
X=scale(X)
dataset2= dataset1.drop(["Stock Return"], axis =1)

pca= PCA(n_components =26)    #n_components=7 as there are 26 columns
pca.fit(X)

print(pca.explained_variance_)
print(pca.explained_variance_ratio_)

pca= PCA(n_components =7)    #only 7 varaiable has eigen value >1 so now only those 7 are taken
pca.fit(X)

result = pd.DataFrame(pca.components_).T