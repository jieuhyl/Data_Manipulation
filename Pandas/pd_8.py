# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 22:48:33 2020

@author: Jie.Hu
"""

import numpy as np
import pandas as pd

# read data
df = pd.read_csv('survey_results_public.csv', index_col = 'Respondent')
df_schema = pd.read_csv('survey_results_schema.csv', index_col = 'Column')


# mean, median and percentile
df['ConvertedComp'].mean()
df['ConvertedComp'].median()
df[df['ConvertedComp'] < 200000]['ConvertedComp'].quantile([.1, .3, .5, .8, 1])


# counts
df['Hobbyist'].value_counts()
df['SocialMedia'].value_counts(normalize = True)

df[df['Country'] == 'United States']['SocialMedia'].value_counts(normalize = True)


# group by 
df.groupby(['Country'])['SocialMedia'].value_counts().loc['China']

df.groupby(['Country'])['ConvertedComp'].mean().loc[['China', 'India', 'United States']]

df.groupby(['Country'])['ConvertedComp'].agg(['mean', 'median', 'count']).loc[['China', 'India', 'United States']]

df.groupby(['Country'])['ConvertedComp'].describe().loc[['China', 'India', 'United States']]

df[['Country', 'ConvertedComp']].groupby(['Country'], as_index=False).mean().sort_values(by='ConvertedComp', ascending=False)


# extra
a = df['Country'].value_counts()
b = df.groupby(['Country'])['LanguageWorkedWith'].apply(lambda x: x.str.contains('Python').sum())
c = pd.concat([a, b], axis = 1)

c['pct'] = round(c['LanguageWorkedWith']/c['Country'], 2)
c.sort_values(by = 'pct', ascending = False, inplace = True)

c.loc[['Japan', 'South Korea']]
c.loc['China', 'pct']