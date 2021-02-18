t = int(input())
for _ in range(t):
    n, k, X, Y = map(int,input().split())
    if X == Y:
        print(n,n)
    else:
        x = [X,0,0,0,0]
        y = [Y,0,0,0,0] 
        if X>Y:
            x[1] = n
            y[1] = Y+n-X
            x[2] = y[1]
            y[2] = x[1]
            x[3] = 0
            y[3] = n-x[2]
            x[4] = y[3]
            y[4] = x[3]
        else:
            x[1] = X+n-Y
            y[1] = n
            x[2] = y[1]
            y[2] = x[1]
            x[3] = n-y[2]
            y[3] = 0
            x[4] = y[3]
            y[4] = x[3]
        if k%4==0:
            print(x[4],y[4])
        elif k%4==1:
            print(x[1],y[1])
        elif k%4==2:
            print(x[2],y[2])
        else:
            print(x[3],y[3])
        
