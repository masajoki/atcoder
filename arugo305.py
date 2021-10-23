N=int(input())
dp=[0 for _ in range(N+1)]
dp[0]=1
for i in range(N+1):
    if i>=3:
        dp[i]=max(dp[i],dp[i-3]+dp[i-2]+dp[i-1])
    elif i>=2:
        dp[i]=max(dp[i],dp[i-2]+dp[i-1])
    elif i>=1:
        dp[i]=max(dp[i],dp[i-1])

print(dp[N])
