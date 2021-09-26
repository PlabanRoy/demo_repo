# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:30:21 2019

@author: plaba
"""


def diagonalDifference(arr):
    # Write your code here
    prim =0
    sec=0
    length = len(arr[0])
    i=0
    for count in range(length):
        prim += arr[count][count]
        sec += arr[count][(length-count-1)]
    return abs(prim-sec)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
