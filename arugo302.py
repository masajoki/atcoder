N=int(input())
dp=[0 for _ in range(N+1)]
dp[0]=1
for i in range(N+1):
    if 2>i>=1:
        dp[i]=max(dp[i-1],dp[i])
    elif i>=2:
        dp[i]=max(dp[i-1]+dp[i-2],dp[i])
    else:
        dp[i+1]=dp[i]
print(dp[N])
