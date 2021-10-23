N,M=map(int,input().split())
W=list(map(int,input().split()))
V=list(map(int,input().split()))
dp=[[0 for _ in range(M+1)]for _ in range(N+1)]


for i in range(N): #ボールの番号
    for m in range(M+1): #重さがM以下
        if m-W[i]>=0:
            dp[i+1][m]=max(dp[i+1][m],dp[i][m-W[i]]+V[i])
        dp[i+1][m]=max(dp[i+1][m],dp[i][m])

print(dp[N][M])