t = int(input())
d={}
for i in range(16):
    x = bin(i).replace("0b", "").zfill(4)
    d[x]=chr(i+97)
for _ in range(t):
    n = int(input())
    s = input()
    ans = ""
    for i in range(0,n,4):
        for j in d.keys():
            if s[i:i+4]==j:
                ans+=d[j]
                break
    print(ans)
