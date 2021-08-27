H,W,C=map(int,input().split())
A=[]
for i in range(H):
    a=list(map(int,input().split()))
    A.append(a)

ans=float("inf")

dp=[[float("inf") for _ in range(W+1)]for _ in range(H+1)]
dp[0][0]=A[0][0]
for i in range(H):
    for j in range(W):
        if i-1>=0:
            dp[i][j]=min(dp[i][j],dp[i-1][j]+C)
        if j-1>=0:
            dp[i][j]=min(dp[i][j],dp[i][j-1]+C)
        if not (i==H-1 and j==W-1):
            dp[i][j]=min(A[i][j],dp[i][j])


for i in range(H):
    for j in range(W):
        if i-1>=0:
            ans=min(ans,dp[i-1][j]+C+A[i][j])
        if j-1>=0:
            ans=min(ans,dp[i][j-1]+C+A[i][j])


#左右を逆にしてもう一回
for i in range(H):
    A[i].reverse()


dp=[[float("inf") for _ in range(W+1)]for _ in range(H+1)]
dp[0][0]=A[0][0]
for i in range(H):
    for j in range(W):
        if i-1>=0:
            dp[i][j]=min(dp[i][j],dp[i-1][j]+C)
        if j-1>=0:
            dp[i][j]=min(dp[i][j],dp[i][j-1]+C)
        if not (i==H-1 and j==W-1):
            dp[i][j]=min(A[i][j],dp[i][j])


for i in range(H):
    for j in range(W):
        if i-1>=0:
            ans=min(ans,dp[i-1][j]+C+A[i][j])
        if j-1>=0:
            ans=min(ans,dp[i][j-1]+C+A[i][j])


print(ans)
