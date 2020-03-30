# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 23:02:45 2020

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

# subset
df[df['first']=='a']
df.loc[df['first']=='a', 'number']


df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('survey_results_schema.csv', index_col = 'Column')

df.loc[df['ConvertedComp'] >= 70000, ['Country', 'ConvertedComp']]

df.loc[df['Country'].isin(['United States', 'Germany']), ['Country', 'ConvertedComp']]

filt = df['LanguageWorkedWith'].str.contains('Python', na = False)
df.loc[filt, 'LanguageWorkedWith']



# mapping =====================================================================
# 1
df['QLF5r2'] = df['QLF5r2'].map({5:1, 4:1, 3:0, 2:0, 1:0}).astype(int)


# 2
df['Title'] = df['Title'].replace(['Capt', 'Don', 'Rev', 'Jonkheer', 'Dona'], 'LowRare')
df['Title'] = df['Title'].replace('Col', 'Master')


# 3
df['QPOSTINT'] = np.where(df['QPOSTINT'] < 2, 1, 0)
df['QPOSTINT'] = np.where(df['QPOSTINT'] < 3, 1, 0)


# 4
df['QPOSTINT'] = df['QPOSTINT'].apply(lambda x: 1 if x==1 else 0)


#5
# divide studio into 4 parts
Studio_counts = df['STUDIO'].value_counts(ascending = False).tolist()
pd.qcut(Studio_counts, 4)
#df['AgeBin'] = pd.qcut(df['Age'], 4)

# create studio counts
df['STUDIO_COUNTS'] = df.groupby(['STUDIO'])['MVID'].transform('count')

# create a group 
def f(row):
    if row['STUDIO_COUNTS'] > 18:
        val = "SUPER"
    elif row['STUDIO_COUNTS'] > 5 and row['STUDIO_COUNTS'] <= 18:
        val = "BIG"
    elif row['STUDIO_COUNTS'] > 2 and row['STUDIO_COUNTS'] <= 5:
        val = "MEDIUM"
    else:
        val = "SMALL"
    return val

df['STUDIO_GROUP'] = df.apply(f, axis=1)

# 6
# create a group 
def f(row):
    if row['OBO'] <= 10:
        val = 1
    elif row['OBO'] > 10 and row['OBO'] <=50:
        val = 2
    elif row['OBO'] > 50 and row['OBO'] <=100:
        val = 3
    else:
        val = 4
    return val
bo['Group'] = bo.apply(f, axis=1)

def f2(row):
    if row <= 10:
        val = 1
    elif row > 10 and row <=50:
        val = 2
    elif row > 50 and row <=100:
        val = 3
    else:
        val = 4
    return val
bo['Group'] = bo['OBO'].apply(f)

# 7
df.columns.get_loc('QSTORYLINESr1') 
df.columns.get_loc('QSTORYLINESr12')

def mapping(x):
    if x==1:
        val = 1
    else:
        val = 0
    return val
   
df.iloc[:,93:105] = df.iloc[:,93:105].applymap(mapping)




