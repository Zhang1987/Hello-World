# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 16:34:52 2019

@author: sunzh
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
from scipy.stats import norm
from scipy import stats
from pandas import DataFrame

import os
os.chdir(r'C:\Users\sunzh\Desktop\Kaggle\House_prices')

train_df=pd.read_csv('train.csv', index_col=0)
test_df=pd.read_csv('test.csv',index_col=0)

train_df.head()

train_df.describe() 