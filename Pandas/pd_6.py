# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:27:18 2020

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

# add col
df['name'] = df['first'] + '_' + df['last']
df['number5'] = df['number'] + 5

# drop col
df.drop(['name', 'number5'], axis = 1, inplace = True)



# add row
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df1

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df3 = df1.append(df2, ignore_index = True)

# drop row
df3.drop(index = [2,3], inplace = True)
df3.drop(index = df3[df3['A'] == 1].index)



# cancate =====================================================================
df1 = pd.DataFrame([['a', 1], ['b', 2]],
                   columns=['letter', 'number'])
df2 = pd.DataFrame([['c', 3], ['d', 4]],
                   columns=['letter', 'number'])
pd.concat([df1, df2], ignore_index = True)



# merge =======================================================================
df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [1, 2, 3, 5]})
df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
                    'value': [5, 6, 7, 8]})

df3 = pd.merge(df1, df2, left_on=['lkey'], right_on=['rkey'], how='left')
