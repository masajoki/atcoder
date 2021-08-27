N=int(input())
dp=[float("inf") for _ in range(100000+10)]
sixes=(6**0,6**1,6**2,6**3,6**4,6**5,6**6)
nines=(9**0,9**1,9**2,9**3,9**4,9**5,9**6)
dp[0]=0
for i in range(1,N+1):
    for s in sixes:
        if i-s>=0:
            dp[i]=min(dp[i],dp[i-s]+1)
    for n in nines:
        if i-n>=0:
            dp[i]=min(dp[i],dp[i-n]+1)
    if i-1>=0:
        dp[i]=min(dp[i],dp[i-1]+1)
print(dp[N]) 
