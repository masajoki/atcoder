dp= [0 for _ in range(10**6+10)]
dp[3]=1
N=int(input())

for i in range(4,N+1):
    dp[i]=(dp[i-1]+dp[i-2]+dp[i-3] )%10007

print(dp[N])

