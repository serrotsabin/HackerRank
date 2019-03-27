#!/bin/python3

import os
import sys

#
# Complete the breakingRecords function below.
#
def breakingRecords(score):
    #
    # Write your code here.
    #
    h=score[0]
    l=score[0]
    n=len(score)
    c1=0
    c2=0
    i=0
    for i in range(n):
        if h<score[i]:
            h = score[i]
            c1 = c1 + 1
        if l>score[i]:
            l = score[i]
            c2 = c2 +1
    return(c1 , c2) 

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    score = list(map(int, input().rstrip().split()))

    result = breakingRecords(score)

    f.write(' '.join(map(str, result)))
    f.write('\n')

    f.close()
