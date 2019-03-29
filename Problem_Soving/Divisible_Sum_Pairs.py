#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    i=0
    j=0
    c=0
    d=0
    e=0
    for i in range(n):
        for j in range(n):
            if i == j:
                break
            c = ar[i]+ar[j]
            e = c%k
            if e==0:
                d=d+1
    result=d
    return(result)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
