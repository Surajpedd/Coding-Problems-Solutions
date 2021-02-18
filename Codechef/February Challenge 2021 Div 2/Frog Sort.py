def getind(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i

def frogsort(W,L,n):
    pos = [i for i in range(n)]
    sor = sorted(W)
    count = 0
    for i in range(1,n):
        ind = getind(W,sor[i])
        p = pos[getind(W,sor[i-1])]
        c = ind
        while(c<=p):
            c+=L[ind]
            pos[ind] = c
            count+=1
    return count
        
t = int(input())
for _ in range(t):
    n = int(input())
    W = list(map(int,input().split()))
    L = list(map(int,input().split()))
    if n == 2:
        if W[0] == 1:
            print(0)
        else:
            if L[0] == 1:
                print(2)
            else:
                print(1)
    else:
        print(frogsort(W,L,n))
