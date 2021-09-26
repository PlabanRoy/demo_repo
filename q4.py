# -*- coding: utf-8 -*-
"""
Created on Sat May 25 08:45:51 2019

@author: plaba
"""

a=list()
number=int (input ('enter ur no. of elements'))
print('enter the elements')
count=0

for i in range  (number):
    n=int (input ('number'))
    a.append (int (n))
    if n>= 0:
        count=count+1
print('positive',count);
print('negative',number-count);
        
        
    
        