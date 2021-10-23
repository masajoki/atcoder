N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
dp=[[ -1 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0]=0
for i in range(N-1):
    for j in range(M):
        if j-A[i]>=0 and dp[i][j-A[i]]!=-1:
            dp[i+1][j]=max(dp[i+1][j],dp[i][j-A[i]]+B[i])
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
                
if dp[N-1][M-1]==0:
    print(-1)
else:
    print(dp[N-1][M-1])