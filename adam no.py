# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 10:17:58 2019

@author: plaba
"""
import math
n=int(input('enter no.'))
sq=0
rev=0
rem=int
while(n>0):
    sq=n*n
    temp=sq
    print(temp)
    while(sq>0):
        rem=n%10
        rev=rev*10+rem
        sq=sq//10
X=(math.sqrt(rev))
y=X
rem=n%10
rev=rev*10+rem
X=X//10
if (rev==n):
    print('yes')
    
    