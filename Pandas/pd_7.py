# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:28:42 2020

@author: Jie.Hu
"""

import numpy as np
import pandas as pd


# dictionary to dataframe
people = {'first':['a', 'b', 'c'],
          'last': ['aa', 'bb', 'cc'],
          'number': [1,2,3]}

# 
df = pd.DataFrame(people)

#sort
df.sort_values(by = 'last', ascending = False)

df.sort_values(by = ['last', 'first'], ascending = [False, True], inplace = True)

df.sort_index(inplace = True)


df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('survey_results_schema.csv', index_col = 'Column')


df['ConvertedComp'].nlargest(10)
df.nlargest(10, 'ConvertedComp')

df['ConvertedComp'].nsmallest(10)
df.nsmallest(10, 'ConvertedComp')
