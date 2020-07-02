n=int(input())
fact={}
for i in range(1,n+1):
    if n%i==0:
        fact[i]=sum(map(int,str(i)))
for i in fact.keys():
    if fact[i]==max(fact.values()):
        print(i)
        break

