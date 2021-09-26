# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:07:30 2019

@author: plaba
"""

n=int(input('enter the num'))
rev=0
rem=int
temp =n
while (n!=0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
if(temp==rev):
    print('yes')
else:
    print('no')