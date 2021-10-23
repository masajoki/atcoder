S=input()
T=input()

dp=[[10**10 for _ in range(len(T)+1)]for _ in range(len(S)+1)]
dp[0][0]=0
for i in range(len(S)):
    for j in range(len(T)):
        if S[i]==T[j]:
            dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j],dp[i+1][j]+1,dp[i][j+1]+1)
        else:
            dp[i+1][j+1]=min(dp[i+1][j+1],dp[i][j]+1,dp[i+1][j]+1,dp[i][j+1]+1)

print(dp)
print(dp[len(S)][len(T)])