# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:27:03 2019

@author: plaba
"""

def is_leap(year):
    leap = False
      # Write your logic here
year =int(input())
if year%100==0 :
    print('False')
elif year%4==0:
    print('True') 
else:
    return leap                             