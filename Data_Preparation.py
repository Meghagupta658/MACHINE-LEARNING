#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:04:19 2021

@author: meghagupta
"""

#to fill missing values in an excel
import numpy as np
import pandas as pd
dataset = pd.read_excel('Time Series.xlsx' ,sheet_name = 1)
dataset 
dataset['Sales'].mean()
dataset['Sales'] = dataset['Sales'].fillna(48.3)
dataset['Gender'].mode()
dataset['Gender'] = dataset['Gender'].fillna('Male')
dataset 

#to convert string to numerical in dataset
from sklearn import preprocessing
label_encoder = preprocessing.LabelEncoder()    #LabelEncoder encode labels with a value between 0 and n_classes-1 where n is the number of distinct labels.
dataset['Gender'] = label_encoder.fit_transform(dataset['Gender'])
dataset

#to remove duplicate
dataset1 = dataset.drop_duplicates()

