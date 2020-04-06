# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 01:19:20 2020

@author: Jie.Hu
"""


# remove dup

data = open('email.txt', 'r').readlines()

data = [x.strip() for x in data]

data_set = set(data)

cleandata = open('clean.txt', 'w')

for line in data_set:
    cleandata.write(line)
    
    
# 2        
with open('email.txt', 'r') as test_f, open('clean.txt', 'w') as result_f:
    
    for line in set(test_f):
        result_f.write(line)        