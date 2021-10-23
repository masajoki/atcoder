N,M=map(int,input().split())
A=list(map(int,input().split()))
dp=[[ 0 for _ in range(M+1)] for _ in range(N+1)]
dp[0][0]=1
for i in range(N-1):
    for j in range(M):
        if j-A[i]>=0:
            dp[i+1][j]+=dp[i][j-A[i]]
        dp[i+1][j]+=dp[i][j]

ans=0
for t in dp[N-1]:
    if t!=0:
        ans+=1
print(ans)