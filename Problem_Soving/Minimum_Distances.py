#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    i=0
    j=0
    e = len(a)
    c=0
    for i in range(n):
        for j in range(n):
            if i==j:
                break
            if a[i]==a[j]:
                d=abs(i-j)
                if d<e:
                    e=d
                    c=1
    if c == 0:
        e= -1
    result = e
    return(e)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
