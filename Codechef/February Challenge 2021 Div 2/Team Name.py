t = int(input())
for _ in range(t):
    n = int(input())
    fun = input().split()
    nfun = {}
    for i in fun:
        rem = i[1:]
        if rem in nfun:
            nfun[rem].add(i[0])
        else:
            nfun[rem] = set(i[0])
    ans = 0
    tot = list(nfun.keys())
    for i in range(len(tot)):
        for j in range(i+1,len(tot)):   
            un =len(nfun[tot[i]].union(nfun[tot[j]]))
            ans += (un-len(nfun[tot[i]]))*(un-len(nfun[tot[j]]))
    print(2*ans)
