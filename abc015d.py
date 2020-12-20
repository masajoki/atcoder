W=int(input())
N,K=map(int,input().split())

A=[] #幅
B=[] #重要度
ans=0 #重要度の合計の最大値
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)


# 価値で動的計画法、3次元でやってみます。
dp=[[[ 0 for _ in range(K+1) ] for _ in range (W + 1)] for _ in range (N + 1)]

for i in range(N):
    for w in range(W):
        for k in range(K):
            if (w - A[i]) >= 0: #選ぶ
                dp[i+1][w][k+1]=max( dp[i][w-A[i]][k]+B[i],dp[i][w][k])
            else:
                dp[i+1][w][k]=dp[i][w][k]

for i in range(N+1):
    for w in range(W+1):
        for k in range(K+1):
            ans=max(ans,dp[i][w][k])

print(ans)




