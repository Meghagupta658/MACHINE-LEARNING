#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 00:28:16 2021

@author: meghagupta
"""

import pandas as pd
dataset = pd.read_excel("2.Factor Analysis.xlsx",sheet_name = 0)

from sklearn.decomposition import PCA    #PCA Principal Component Analysis is an extraction function
from sklearn.preprocessing import scale  #Scale is used for processing like for any float values to numerical

X = dataset.values
X=scale(X)

pca = PCA(n_components=7)    #n_components=7 as there are 7 columns
pca.fit(X)

print(pca.explained_variance_)   #ca.explained_variance_ this is for printing eigen value which should come as greater than 1 for considering it as factor
print(pca.explained_variance_ratio_)    #this will give how much % each varaiable is contributing

pca = PCA(n_components=3)    #only 3 varaiable has eigen value >1 so now only those 3 are taken
pca.fit(X)

print(pd.DataFrame(pca.components_))
print(pd.DataFrame(pca.components_).T)    #it will transform the matrix it is now factor matrix