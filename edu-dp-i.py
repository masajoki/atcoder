N=int(input())
dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
P=list(map(float,input().split()))

dp[1][0]=1-P[0]
dp[1][1]=P[0]
for i in range(1,N):
    for j in range(0,N+1):
        if j-1>=0:
            dp[i+1][j]=dp[i][j]*(1-P[i])+dp[i][j-1]*P[i]
        else:
            dp[i+1][j]=dp[i][j]*(1-P[i])
            
ans=0
for i in range(N//2+1,N+1):
    ans+=dp[N][i]
print(ans)

#割と基本的なDPだったと思う。サンプル問題の答え見間違えて何度も逡巡してしまった。