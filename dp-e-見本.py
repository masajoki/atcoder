N,W=map(int,input().split())
v,w=[],[]
max_v=10**5+100
inf=1<<30
dp=[[inf]*(max_v) for i in range(N+1)]
dp[0][0]=0
for i in range(N):
    we,va=map(int,input().split())
    w.append(we)
    v.append(va)

for i in range(N):
    for j in range(max_v):
        if j-v[i]>=0:
            dp[i+1][j]=min(dp[i][j-v[i]]+w[i],dp[i][j])
        else:
            dp[i+1][j]=min(dp[i][j],dp[i+1][j])
ans=0
for i in range(max_v):
    if dp[N][i]<=W:
        ans=max(ans,i)
print(ans)
