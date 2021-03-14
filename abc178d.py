N,X,Y=map(int,input().split())
dp=[N+1 for _ in range(N+1)]
dp[0]=0
def updatedp(start):
    if start -1 >=0:
        if dp[start-1] > dp[start]+1:
            dp[start-1]=dp[start]+1
            updatedp(start-1)
    if start +1 <=N:
        if dp[start+1] > dp[start]+1:
            dp[start+1]=dp[start]+1
            updatedp(start+1)
    if start ==X:
        if dp[Y]>dp[X]+1: 
            dp[Y]=dp[X]+1
            updatedp(Y)
    if start ==Y:
        if dp[X]>dp[Y]+1: 
            dp[X]=dp[Y]+1
            updatedp(X)

ans=[0 for _ in range(N+1)]
for i in range(N):
    updatedp(i)
    for j in range(N):
        ans[j]+=dp.count(j+1)
    
print(ans)

