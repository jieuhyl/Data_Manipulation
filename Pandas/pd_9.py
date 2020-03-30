# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:47:47 2020

@author: Jie.Hu
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

people = {'first':['Corey', 'Jane', 'John','Chris', np.nan, None, 'NA'],
          'last': ['Schafer', 'Doe', 'Doe', 'Schafer', np.nan, np.nan, 'Missing'],
          'email': ['CoreySchafer@gmail.com','JaneDoe@gmail.com', 'JohnDoe@gmail.com', None, np.nan, 'Anonymous@email.com', 'NA'],
          'age': ['33', '55', '65', '35', None, None, 'Missing']}

df = pd.DataFrame(people)

df.dtypes


# replace
df.replace(['NA', 'Missing'], np.nan, inplace = True)

# check missing
df.isnull().values.sum()
df.isnull().sum()
df.isnull().mean()
missing_ratio = df.isnull().sum() / len(df)

sns.heatmap(df.isnull(), yticklabels=False, cbar=False, cmap='viridis')


# clean all the missings
df.dropna()
# by threshold
df.dropna(thresh = df.shape[0]*0.6, how='all', axis=1)
# or 
df.loc[:, df.isnull().mean() < 0.8]


# filling
df.fillna('Miss', inplace = False)


# filled in missings
# 1 baisc
df['age'] = df['age'].astype(float)
df['age'].fillna(100) 
df['age'].fillna(df['age'].mean()) 
df['age'].fillna(df['age'].median()) 
df['age'].fillna(df['age'].mode()[0])



# 2 use other group info
df[['FCO_0.5W_T', 'FCO_0.5W_M24', 'FCO_0.5W_M26', 'FCO_0.5W_F24', 'FCO_0.5W_F26', 'CATEGORY']].groupby('CATEGORY').median()
def impute_FCO(cols):
    FCO = cols[0]
    GROUP = cols[1]
    
    if pd.isnull(FCO):

        if GROUP == "A":
            return 42.5
        elif GROUP == "B":
            return 25    
        elif GROUP == "C":
            return 14
        else:
            return 7

    else:
        return FCO
df['FCO_0.5W_T'] = df[['FCO_0.5W_T','CATEGORY']].apply(impute_FCO, axis=1)


# 3, using mean and std
# Age
fig, (axis1,axis2) = plt.subplots(1,2,figsize=(12,4))
axis1.set_title('Original Age values - Titanic')
axis2.set_title('New Age values - Titanic')
# axis3.set_title('Original Age values - Test')
# axis4.set_title('New Age values - Test')

# get average, std, and number of NaN values in train
average_age_train   = train["Age"].mean()
std_age_train       = train["Age"].std()
count_nan_age_train = train["Age"].isnull().sum()

# get average, std, and number of NaN values in test
average_age_test   = test["Age"].mean()
std_age_test       = test["Age"].std()
count_nan_age_test = test["Age"].isnull().sum()

# generate random numbers between (mean - std) & (mean + std)
rand_1 = np.random.randint(average_age_train - std_age_train, average_age_train + std_age_train, size = count_nan_age_train)
rand_2 = np.random.randint(average_age_test - std_age_test, average_age_test + std_age_test, size = count_nan_age_test)

# plot original Age values
# NOTE: drop all null values, and convert to int
train['Age'].dropna().astype(int).hist(bins=70, ax=axis1)
# test['Age'].dropna().astype(int).hist(bins=70, ax=axis3)

# fill NaN values in Age column with random values generated
train["Age"][np.isnan(train["Age"])] = rand_1
test["Age"][np.isnan(test["Age"])] = rand_2

# convert from float to int
train['Age'] = train['Age'].astype(int)
test['Age']    = test['Age'].astype(int)


# 4 using modeling
# Age
from sklearn.ensemble import RandomForestRegressor
data_sub = data[['Age','FamilySize','Sex','Pclass_1', 'Pclass_2']]

x_age_train  = data_sub.dropna().drop('Age', axis=1)
y_age_train  = data['Age'].dropna()
x_age_test = data_sub.loc[np.isnan(data.Age)].drop('Age', axis=1)

regressor = RandomForestRegressor(n_estimators = 400)
regressor.fit(x_age_train, y_age_train)
y_age_pred = np.round(regressor.predict(x_age_test),1)
data.Age.loc[data.Age.isnull()] = y_age_pred

data.isnull().sum(axis=0) # no more NAN now

