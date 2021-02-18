t=int(input())
for q in range(t):
    n,k=map(int,input().split())
    L=list(input())
    i=0
    j=0
    choose=0
    while i<n and j<n:
        if L[i]=='M':
            if L[j]=='I':
                if i>j:
                    p=k+1-(i-j)-L[j:i].count(':')
                else:
                    p=k+1-(j-i)-L[i:j].count(':')
                if p>0:
                    choose+=1
                    i+=1
                    j+=1
                else:
                    if i<j:
                        i+=1
                    else:
                        j+=1
            elif L[j]=='X':
                j+=1
                i=j
            else:
                j+=1
        elif L[i]=='X':
            i+=1
            j=i
        else:
            i+=1
    print(choose)
