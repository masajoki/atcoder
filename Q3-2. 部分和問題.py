N,M=map(int,input().split())
W=list(map(int,input().split()))
dp=[[0 for _ in range(M+1)] for _ in range(N+1)]

dp[0][0]=1
for i in range(N):
    for j in range(M+1):
        if j-W[i]>=0:
            dp[i+1][j]=max(dp[i+1][j],dp[i][j-W[i]])
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])#選ばない

if dp[N][M]!=0:
    print("Yes")
else:
    print("No")