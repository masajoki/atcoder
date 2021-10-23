N,M=map(int,input().split())
W=list(map(int,input().split()))
dp=[[ 10**10 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
    for m in range(M+1):
        dp[i+1][m]=min(dp[i][m],dp[i+1][m])
        if m-W[i]>=0:
            dp[i+1][m]=min(dp[i][m-W[i]]+1,dp[i+1][m])
        
if dp[N][M]==10**10:
    print(-1)
else:
    print(dp[N][M])
