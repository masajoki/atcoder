N,M=map(int,input().split())
A=list(map(int,input().split()))
P=[ [] for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    P[x].append(y)

dp=[[10**10,0] for _ in range(N+10)]

for i in range(N+1):
    x=i
    for y in P[x]:
        if y!=0:
            dp[x][0]=min(dp[x][0],A[x-1])
            dp[y][0]=min(dp[y][0],dp[x][0])
            dp[y][1]=max(dp[y][1],A[y-1])

ans=-999999999999
for d in dp:
    ans=max(ans,d[1]-d[0])
print(ans)
