N=int(input())
A=[]
for i in range(N):
    a=int(input())
    A.append(a)

dp=[[-1 for _ in range(101)] for _ in range(N+1)]

dp[0][0]=0
for i in range(N):
    for j in range(101):
        dp[i+1][j]=max(dp[i+1][j],dp[i][j])
        if 100>=j-A[i]>=0:
            dp[i+1][j]=max(dp[i][j-A[i]],dp[i+1][j])


M=dp[N].count(0)
print(M)
for i in range(101):
    if dp[N][i]==0:
        print(i)