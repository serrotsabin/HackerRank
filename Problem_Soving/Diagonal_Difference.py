#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    #
    # Write your code here.
    #
    d1 = 0
    d2 = 0
    i = 0
    j = 0
    x = 0
    result = 0
    n = len(a)
    for i in range(n):
        for j in range(n):
            if (i == j):
                d1 = d1 + a[i][j]    
    i=0
    j=n-1
    while i < n :
        d2 = d2 +a[i][j]
        i=i+1
        j=j-1
    result = abs(int(d1) - int(d2))
    return(result)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()