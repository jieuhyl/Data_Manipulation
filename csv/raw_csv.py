# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:45:46 2020

@author: Jie.Hu
"""

import os
import csv

print("Current Working Directory " , os.getcwd())
os.chdir(r'C:\Users\Jie.Hu\Desktop\data\csv')

# 1
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    next(csv_reader)
    
    for line in csv_reader:
        print(line)
        

# 2              
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    
    with open('new_names.csv', 'w', newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter = '\t')
        
        for line in csv_reader:
            csv_writer.writerow(line)       
            
            
# 3
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = '\t')
    
    for line in csv_reader:
        print(line)           
        
        

# 4
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)
        
        

# 5
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(new_file, fieldnames = fieldnames, delimiter = '\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
            
            
# 6 
with open('new_names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for line in csv_reader:
        print(line)            