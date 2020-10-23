t=int(input())
for i in range(t):
    L=list(map(int,input().split(" ")))
    ncity=L[2]
    i=0;
    while i<L[0]:
        ncity=(ncity+L[1])%L[0]
        if L[3] == ncity:
            print("YES")
            break
        i+=1
    else:
        print("NO")
    
