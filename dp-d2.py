N,W=map(int,input().split())
w=[]
v=[]
for i in range(N):
    wt,vt=map(int,input().split())
    w.append(wt)
    v.append(vt)

dp= [ [0 for _ in range(W+10)]  for _ in range(N+10)]


for i in range(N):
    for wl in range(W+1):
        if  wl - w[i] >= 0:
            dp[i+1][wl]=max(dp[i][wl],dp[i][wl-w[i]]+v[i])
        else:
            dp[i+1][wl]=dp[i][wl]

print(max(dp[N]))
