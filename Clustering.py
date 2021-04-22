#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 12:04:00 2021

@author: meghagupta
"""

import pandas as pd
import numpy as np
from scipy.cluster import hierarchy    #hierarchy function mainly used for clustering
import matplotlib.pyplot as plt
dataset = pd.read_excel("2 Cluster Analysis.xlsx",sheet_name = 0)

dist=np.array(dataset)    #to calculate eucidean distance
Z=hierarchy.linkage(dist,'average')   #average link is applied 
plt.figure()
dn=hierarchy.dendrogram(Z)    # representation of clusters in pictorial format
