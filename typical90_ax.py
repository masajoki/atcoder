N,L=map(int,input().split())
dp=[0 for _ in range(N+1)]
dp[0]=1
for i in range(N+1):
    if i-1>=0:
        dp[i]+=dp[i-1]
    if i-L>=0:
        dp[i]+=dp[i-L]

print(dp[N]%(10**9+7))