# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:59:52 2020

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

# change column names
df.columns = [x.upper() for x in df.columns]
df.columns = df.columns.str.replace('ST', '_')

# alter cell values
df.loc[2, 'NUMBER'] = 5
df.loc[1, ['FIRST', 'LAST']] = ['D', 'DD']

# lower case
df['FIRST'] = df['FIRST'].str.lower()

# apply
def addone(num):
    return num+1
df['NUMBER2'] = df['NUMBER'].apply(addone)

def addten(row):
    return row['NUMBER2'] + 10
df['NUMBER3'] = df.apply(addten, axis = 1)

# applied to columns
df.apply(len, axis = 1)
# applied to rows
df.apply(len, axis = 0)
# applied to data
df.applymap(len)


# add col
df['NAME'] = df['FIRST'] + '_' + df['LAST']
df['NUMBER4'] = df['NUMBER'] + 5

# drop col
df.drop(['NAME', 'NUMBER4'], axis = 1, inplace = True)


# add row
df1 = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df1

df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df3 = df1.append(df2, ignore_index = True)

# drop row
df3.drop(index = [2,3], inplace = True)
df3.drop(index = df3[df3['A'] == 1].index)

