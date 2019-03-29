#!/bin/python3

import sys

def equalizeArray(arr):
    # Complete this function
    i = 0
    j = 0
    n = len(arr)
    cm = 0
    for i in range(n):
        c=0
        for j in range(n):
            if(arr[i]==arr[j]):
                c = c +1
        if c > cm:
            cm=c
    result = n - cm
    return(result)
    
if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    result = equalizeArray(arr)
    print(result)
