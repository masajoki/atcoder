N,M=map(int,input().split())
A=list(map(int,input().split()))

l=10**10
dp=[l for _ in range(N+1)]
dp[0]=0
for i in range(N):
    for j in range(1,M+1):
        if i-j>=0:
            dp[i]=min(dp[i],dp[i-j]+j*A[i])

print(dp[N-1])
