# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 08:56:40 2019

@author: plaba
"""
def identical(a,b):
    count=0
    for i in range((len (a)-1)):
        for j in range((len (b)-1)):
            if a[i]==b[j]:
                count+=1
    if count==n:
        print(1)





a=[]
n= 2
for r in range(n):
    x=int(input())
    a.append(x)
b=[int(input()) for j in range (n)]
identical(a,b)


