N,M=map(int,input().split())
dp=[0 for _ in range(N+10)]
bad=[False for _ in range(N+10)]
mod=10**9+7


for i in range(M):
    a=int(input())
    bad[a]=True

dp[0]=1
if bad[1]!=True:
    dp[1]=1
    
for i in range(2,N+1):
    if bad[i]!=True:
        dp[i]=(dp[i-1]+dp[i-2])%mod
        # dp[i]=(dp[i-1]+dp[i-2])
print(dp[N]%mod)
