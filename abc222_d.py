# abc222_d
# 累積和と動的計画法の組み合わせ

N = int(input())
MOD = 998244353
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp=[[ 0 for _ in range(3000+10)]for _ in range(3000+10) ]
for i in range(A[0],B[0]+1):
    dp[0][i]=dp[0][i-1]+1

for i in range(N):
    for j in range(3000+10):
        if A[i]<=j<=B[i]:
            dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[i][j-1])%MOD
        else:
            dp[i][j]=max(dp[i][j],dp[i][j-1])%MOD        
print(dp[N-1][B[-1]]%MOD)
