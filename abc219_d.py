N=int(input())
X,Y=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

if sum(A)<X or sum(B)<Y:
    print(-1)
    exit()

dp=[[[999 for _ in range(Y+1)] for _ in range(X+1)] for _ in range(N+1)]
dp[0][0][0]=0
for i in range(1,N+1):
    for j in range(X+1):
        for k in range(Y+1):
            a=A[i-1]
            b=B[i-1]    
            x=j+a
            y=k+b
            x=max(x,X)
            y=max(y,Y)
            if i==0:
                continue
            else:
                b4jump=dp[i-1][j][k]
                dp[i][j][k]=min(dp[i][j][k],b4jump)
                dp[i][x][y]=min(dp[i][x][y],dp[i-1][x][y],b4jump+1)

if dp[N][X][Y]>=999:
    print(-1)
else:
    print(dp[N][X][Y])

#こういうの配るDPっていうのかな？
#3次元配るDPで、配布先がXとYを超えたときに最大値に揃える必要がある
# float('inf')を使うとTLEしてしまう
