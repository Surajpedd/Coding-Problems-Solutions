#!/bin/python3
import os
import sys

def fact(k):
    f=1
    for i in range(2,k+1):
        f=f*i
    return f
# Complete the solve function below.
def solve(n, m):
    return fact(m+n-1)//(fact(m-1)*fact(n))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nm = input().split()

        n = int(nm[0])

        m = int(nm[1])

        result = solve(n, m)%((10**9)+7)

        fptr.write(str(result) + '\n')

    fptr.close()
