N,K=map(int,input().split())
H=list(map(int,input().split()))
dp=[(10**9+7) for _ in range(N+1)]

dp[0]=0
for i in range(1,N):
    for k in range(1,K+1):
        if i-k<0:
            continue
        t=dp[i-k]+abs(H[i]-H[i-k])
        dp[i]=min(t,dp[i])
print(dp[N-1])

