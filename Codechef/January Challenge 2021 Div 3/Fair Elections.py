t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    f = 1
    for i in range(min(m,n)+1):
        if sum(A[i::]) + sum(B[:m-i-1:-1]) > sum(B[:m-i:]) + sum(A[:i:]):
            print(i)
            f = 0
            break
    if f:
        print(-1)
