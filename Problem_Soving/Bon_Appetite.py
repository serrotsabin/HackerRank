# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3

import sys

#
def bonAppetit(n, k, b, ar):
    total=sum(ar)
    extra=ar[k]
    avg=(total-extra)/2
    r=b-int(avg)
    if r==0:
        return("Bon Appetit")
    else:
        return(r)

n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
ar = list(map(int, input().strip().split(' ')))
b = int(input().strip())
result = bonAppetit(n, k, b, ar)
print(result)