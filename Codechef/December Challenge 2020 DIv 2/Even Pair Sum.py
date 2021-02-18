t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    if a%2==0 and b%2==0:
        c = (a//2)*(b//2)*2
    elif a%2==0 and b%2!=0:
        c = (a//2)*( 2*(b//2) + 1)
    elif a%2!=0 and b%2==0:
        c = (b//2)*( 2*(a//2) + 1)
    else:
        c = (a//2 + 1)*(b//2 + 1) + (a//2)*(b//2)
    print(c)
