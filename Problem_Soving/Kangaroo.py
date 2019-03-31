#!/bin/python3

import sys

def kangaroo(x1, v1, x2, v2):
   
    a = x1
    b = x2
    if x1>x2 and v1>v2 or x1<x2 and v1<v2:
        return("NO")
    else:
        if a == b:
            return("YES")
        else:
            a = x1 + v1
            b = x2 + v2
            for i in range(0,10000):
                if a == b:
                    return("YES")
                    break
                a += v1
                b += v2
            else:
                return("NO")

x1, v1, x2, v2 = input().strip().split(' ')
x1, v1, x2, v2 = [int(x1), int(v1), int(x2), int(v2)]
result = kangaroo(x1, v1, x2, v2)
print(result)