t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    a=[]
    x = (-1)**((n+1)%2)
    y = (-1)**(n%2) 
    for j in range(1,n,2):
        a.extend([x*j,y*(j+1)])
    if n%2!=0:
        a.append(n)
    c=(n+1)//2
    sum=0
    for j in a:
        sum+=j
        if sum>0:
            if c==k:
                break
            elif c<k:
                for p in range(n-2,-1,-2):
                    a[p]=-a[p]
                    c+=1
                    if c==k:
                        break
            else:
                for p in range(n-1,-1,-2):
                    a[p]=-a[p]
                    c-=1
                    if c==k:
                        break
    print(*a)
