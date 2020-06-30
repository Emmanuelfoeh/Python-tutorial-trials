# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

h = 4
g = 32
print(h + g)
print("This is my first time doing coding in spyder and i think its cool")
"""

import os
import csv

path = "C:/Users/BLESS/Python_data"
Filepath = os.path.join(path,"panda.csv")

with open(Filepath,"r") as csvFile:
    readMyCsv = csv.reader(csvFile)
    for row in readMyCsv:
        print(row)
    
