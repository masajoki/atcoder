H,W=map(int,input().split())
S=[]
for i in range(H):
    s=list(map(int,input().split()))
    S.append(s)

dp=[[0 for _ in range(W+1)]for _ in range(H+1)]
for i in range(W):
    dp[1][i]=S[0][i]
for i in range(1,H):
    for j in range(W):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j]+S[i][j])
        if 0<=j-1<W:
            dp[i+1][j]= max(dp[i+1][j],dp[i][j-1]+S[i][j])
        if 0<=j+1<W:
            dp[i+1][j]= max(dp[i+1][j],dp[i][j+1]+S[i][j])

print(max(dp[H])) 
