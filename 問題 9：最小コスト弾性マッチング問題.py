N,M=map(int,input().split())
C=[]
for i in range(N):
    c=list(map(int,input().split()))
    C.append(c)

dp=[[10**12 for _ in range(M+1)]for _ in range(N+1)]

dp[0][0]=0
for i in range(N):
    for j in range(M):
        dp[i+1][j+1]=min(dp[i][j],dp[i+1][j],dp[i][j+1])+C[i][j]

print(dp[N][M])

