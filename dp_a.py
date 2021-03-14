N=int(input())
H=list(map(int,input().split()))
dp=[(10**9+7) for _ in range(N+1)]

dp[0]=0
dp[1]=abs(H[1]-H[0])
for i in range(N):
    if i-2 >= 0:
        t1=dp[i-1]+abs(H[i]-H[i-1])
        t2=dp[i-2]+abs(H[i]-H[i-2])
        dp[i]=min(t1,t2)
print(dp[N-1])
　