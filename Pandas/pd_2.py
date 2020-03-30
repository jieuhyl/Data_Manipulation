# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 23:10:52 2020

@author: Jie.Hu
"""


import numpy as np
import pandas as pd


# matrix to dataframe
matrix = [
    ["a", 1],
    ["b", 2]
]
pd.DataFrame(matrix)


# list to array to dataframe
lst = [1,2,3,4]
pd.DataFrame(np.array(lst).reshape(2,2), columns = list("ab"))


# dictionary to dataframe
people = {'first':['a', 'b', 'c'],
          'last': ['aa', 'bb', 'cc'],
          'number': [1,2,3]}

df = pd.DataFrame(people)

df['number']
type(df['number'])

df[['first', 'last']]

df.columns

df.iloc[0,:]
df.iloc[:,0]
df.iloc[[0,2],:]

df.loc[:, ['first', 'last']]
df.loc[1, 'first']
df.loc[1]

# counts
df = pd.read_csv('survey_results_public.csv')
df_schema = pd.read_csv('survey_results_schema.csv')


df['Hobbyist'].value_counts()
df['Hobbyist'].value_counts(normalize = True)

df.loc[0:2, ['Hobbyist', 'Employment']]