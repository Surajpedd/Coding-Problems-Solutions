from math import ceil
d1, v1, d2, v2, p = map(int, input().split())
if d1==d2:
    print( d1-1 + ceil(p/(v1+v2)) )
elif d2>d1:
    if ceil(p/v1) <= (d2-d1):
        print(ceil(p/v1) + d1-1)
    else:
        x = p - (d2-d1)*v1
        print( (d2-d1) + ceil(x/(v1+v2)) + d1-1)
else:
    if ceil(p/v2) <= (d1-d2):
        print(ceil(p/v2) + d2-1)
    else:
        x = p - (d1-d2)*v2
        print( (d1-d2) + ceil(x/(v1+v2)) + d2-1)
