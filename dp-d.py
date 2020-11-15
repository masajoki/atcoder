N,W=map(int,input().split())
w=[0]
v=[0]
for i in range(N):
    wt,vt=map(int,input().split())
    w.append(wt)
    v.append(vt)

dp= [ [0 for _ in range(W+1)]  for _ in range(N+1)]


for i in range(1,N+1):
    for wl in range(1,W+1):
        if  wl - w[i] >= 0:
            dp[i][wl]=max(dp[i-1][wl],dp[i-1][wl-w[i]]+v[i])
        else:
            dp[i][wl]=dp[i-1][wl]

print(max(dp[N]))
