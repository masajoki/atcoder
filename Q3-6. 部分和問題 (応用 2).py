N,A,B=map(int,input().split())
X=list(map(int,input().split()))
dp=[[ 0 for  _ in range(A+1)] for _ in range(N+1)]

dp[0][0]=1
for i in range(N):
    for a in range(A):
        if dp[i][a]!=0:
            mod=(a+X[i])%A
            dp[i+1][mod]=1
        dp[i+1][a]=max(dp[i+1][a],dp[i][a])

if dp[N][B]==1:
    print("Yes")
else:
    print("No")