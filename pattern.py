# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 23:05:29 2019

@author: plaba
"""

"""n=int(input('enter th num of rows'))
for i in range(1,n+1):
    for j in range (n+1,1,-1):
        print(" "+"*")
    print()  """
    
"""n=int(input('enter the rows'))
for i in range(1, n + 1):
    print(' ' * (n - i) + '#' * i)"""

"""n=int(input('enter the number of rows'))       
for i in range(n,0,-1):
   print('*'*i)"""
         
n=int(input('enter the number of rows'))
for i in range (n):
    for j in range(n):
        print('*',end=" ")
    print()
    
"""n=int(input('enter the number of rows'))       
for i in range(n+1):
   print('*'*i)"""