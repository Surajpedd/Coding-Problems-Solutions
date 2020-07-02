n=int(input())
Bin=[]
while n:
    Bin.append(n%2)
    n=n//2
c=0
count=[]
for i in range(len(Bin)):
    if Bin[i]==0:
        count.append(c)
        c=0
    else:
        c+=1
if c!=0:
    count.append(c)
print(max(count))
