N,K=map(int,input().split())
h=list(map(int,input().split()))
dp=[999999999 for _ in range(N)]

def jumpcost(f,t):
    return abs(h[f]-h[t])

dp[0]=0
for i in range(N):
    for j in range(i+1,i+K+1):
        if j < N:
            dp[j]=min(dp[j],dp[i]+jumpcost(i,j))
print(dp[-1])