#!/bin/python3

import os
import sys

#
# Complete the staircase function below.
#
def staircase(n):
    #
    # Write your code here.
    #
    a=" "
    b="#"
    x=n-1
    for i in range(n):
        print(a*x+b*(i+1))
        x=x-1
    return
if __name__ == '__main__':
    n = int(input())
    staircase(n)