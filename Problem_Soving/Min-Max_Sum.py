#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    #
    # Write your code here.
    #
    largest = 0
    smallest = arr[0]
    n = len(arr)
    for i in range(n):
        if largest < arr[i]:
            largest = arr[i]
        if smallest> arr[i]:
            smallest = arr[i]
    maximum = sum(arr) - smallest 
    minimum = sum(arr) - largest 
    print(minimum, maximum)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
