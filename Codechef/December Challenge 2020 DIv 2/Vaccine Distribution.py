t=int(input())
from math import ceil
for i in range(t):
    n,d = map(int, input().split())
    a = list(map(int,input().split()))
    c=0
    if d==1:
        print(n)
    else:
        for i in a:
            if i<=9 or i>=80:
                c+=1
        print(ceil(c/d) + ceil((n-c)/d))

