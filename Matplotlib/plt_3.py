# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 00:10:50 2020

@author: Jie.Hu
"""
     
from matplotlib import pyplot as plt


slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0, 0, 0, 0.1, 0]

plt.figure(figsize=(5,5))

plt.pie(slices, labels = labels, 
        explode = explode, 
        shadow = False,
        startangle = 90, 
        autopct = '%1.1f%%',
        wedgeprops = {'edgecolor': 'black'})

plt.title("My Awesome Pie Chart")
plt.show()
plt.savefig('1.png')
plt.savefig('1.pdf')