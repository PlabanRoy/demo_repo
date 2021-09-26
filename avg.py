# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:35:53 2019

@author: plaba
"""

a=list()
number=int (input('enter the number of elements'))
sum=0
n=int
print ('enter the elements>')
for i in range(number):
    n=int(input('>'))
    a.append (int(n))
    sum=sum+n
print (sum)    

