H,W=map(int,input().split())
A=[]
for i in range(H):
    A.append(input())

dp=[[0 for _ in range(W+1)] for _ in range(H+1)]
dp[1][1]=1
for i in range(1,H+1):
    for j in range(1,W+1):
        if A[i-1][j-1]=='.':
            dp[i][j]=max(dp[i][j],dp[i-1][j]+dp[i][j-1])%(10**9+7)
        else:
            dp[i][j]==0
print(dp[H][W])
