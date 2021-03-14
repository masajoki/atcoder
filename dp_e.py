N,Wmax=map(int,input().split())

W=[]
V=[]
for i in range(N):
    w,v=map(int,input().split())
    W.append(w)
    V.append(v)
Vmax=sum(V)+1

dp=[[ Wmax+1 for _ in range(Vmax+1)] for _ in range(N+1)]
dp[0][0]=0
for i in range(N):
    for j in range(Vmax):
        if j-V[i]>=0:
            dp[i+1][j]=min(dp[i][j],dp[i][j-V[i]]+W[i])
        else:
            dp[i+1][j]=dp[i][j]

for i in range(Vmax,0,-1):
    if dp[N][i] <= Wmax:
        print(i)
        break
