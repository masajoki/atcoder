N=int(input()) #max 10**5
A=list(map(int,input().split())) #A:0-9
# 操作F: 左端xyを削除して(x+y)%10を挿入
# 操作G: 左端xyを削除して(x*y)%10を挿入

F=[[-1 for _ in range(10)] for _ in range(10)]
G=[[-1 for _ in range(10)] for _ in range(10)]
dp=[[0 for i in range(10)] for _ in range(N+1)]


for i in range(10):
    for j in range(10):
        F[i][j]=(i+j)%10
        G[i][j]=(i*j)%10


dp[0][A[0]]=1

for i in range(N-1):
    for j in range(10):
        a=A[i+1]
        f=F[a][j]
        g=G[a][j]
        dp[i+1][f]+=dp[i][j]
        dp[i+1][f]%=998244353
        dp[i+1][g]+=dp[i][j]
        dp[i+1][g]%=998244353
for i in range(10):
    print(dp[N-1][i]%998244353)