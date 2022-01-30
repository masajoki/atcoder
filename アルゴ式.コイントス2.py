N,M=map(int,input().split())
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]

dp[0][0]=0.5
if M!=0:
    dp[0][1]=0.5

for i in range(N):
    for j in range(M+1):
        if j-1>=0:
            dp[i+1][j]=dp[i][j-1]*0.5+dp[i][j]*0.5
        else:
            dp[i+1][j]=dp[i][j]*0.5

print(dp[N-1][M])