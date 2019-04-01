#!/bin/python3

import sys

def migratoryBirds(n, ar):
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in ar:
        if i == 1:
            a += 1
            pass
        elif i == 2:
            b += 1
            pass
        elif i == 3:
            c += 1
            pass
        elif i == 4:
            d += 1
            pass
        elif i == 5:
            e += 1
            pass
    arr = [a,b,c,d,e]
    mx = max(arr)
    for i in range(0,len(arr)):
        if arr[i] == mx:
            return(i+1)
            break

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = migratoryBirds(n, ar)
print(result)