N=int(input())
dp=[[0 for _ in range(N)]for  _ in range(N)]
dp[0][0]=1
for i in range(N):
    for j in range(N):
        if 0<=i-1<N:
            dp[i][j]+=dp[i-1][j]
        if 0<=j-1<N:
            dp[i][j]+=dp[i][j-1]

print(dp[N-1][N-1])
