def find(L,n,x,p):
    m=n
    ret=0
    for i in range(n):
        if L[i] == x:
            if abs(p-i)<m:
                m=abs(p-i)
                ret=i
    return ret

    
t=int(input())
for i in range(t):
    n,x,p,k=map(int,input().split(" "))
    L=list(map(int,input().split(" ")))
    L.sort()
    val=find(L,n,x,p)
    c=0
    if L[val]!=x:
        L[k-1]=x
        L.sort()
        c+=1
    if L[p-1]==x:
        print(c)
        continue
    if p<k and L[p-1]<x:
        print(-1)
        continue
    if p>k and L[p-1]>x:
        print(-1)
        continue
    val=find(L,n,x,p)+1
    print(abs(p-val)+c)
