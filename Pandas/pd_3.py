# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:45:27 2020

@author: Jie.Hu
"""


import numpy as np
import pandas as pd


# dictionary to dataframe
people = {'first':['a', 'b', 'c'],
          'last': ['aa', 'bb', 'cc'],
          'number': [1,2,3]}

# set index
df = pd.DataFrame(people)
df.set_index('first', inplace = True)
df = df.reset_index()


# change column name
df.columns = ['A', 'B', 'C']
df.rename(columns={'A': 'first', 'B': 'last', 'C': 'number'}, inplace=True)


# 
df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('survey_results_schema.csv', index_col = 'Column')
df_schema.loc['Hobbyist']

df_schema.sort_index(ascending = False, inplace = True)
