#アルゴ式.コイントス3.py
N,M,p=map(int,input().split())
#表が出る確率がp%
r=p/100


dp=[[0 for _ in range(M+1)] for _ in range(N+1)]

dp[0][0]=1-r
if M!=0:
    dp[0][1]=r

for i in range(N):
    for j in range(M+1):
        if j-1>=0:
            dp[i+1][j]=dp[i][j-1]*r+dp[i][j]*(1-r)
        else:
            dp[i+1][j]=dp[i][j]*(1-r)

print(dp[N-1][M])