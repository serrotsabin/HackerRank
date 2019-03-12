#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    #
    # Write your code here.
    #
    x =  len(arr)
    i = 0
    p = 0
    n = 0
    z = 0
    for i in range(x):
        if arr[i] == 0:
            z=z+1
        if arr[i] < 0:
            n=n+1
        if arr[i]>0:
            p=p+1
    print("%.6f" % (p/x))
    print("%.6f" % (n/x))
    print("%.6f" % (z/x))
    return    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
