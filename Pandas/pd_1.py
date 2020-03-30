# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 22:56:51 2020

@author: Jie.Hu
"""

import os
import pandas as pd

print("Current Working Directory " , os.getcwd())
os.chdir(r'C:\Users\Jie.Hu\Desktop\data\Pandas')

df = pd.read_csv('survey_results_public.csv')

# basic info
df.shape

df.head(5)

df.info()

df.describe()

df.columns

df_schema = pd.read_csv('survey_results_schema.csv')

df_schema

# see all the data
pd.set_option('display.max_rows', 85)
pd.set_option('display.max_columns', 85)