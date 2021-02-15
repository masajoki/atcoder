import sys
sys.setrecursionlimit(10**6) 
N,M=map(int,input().split())
Path=[[] for _ in range(N+1)]
Roots=[1 for _ in range(N+1)]

for i in range(M):
    x,y=map(int,input().split())
    Path[x].append(y)
    Roots[y]=0

dp=[-1 for _ in range(N+1)]

def dfs(root,cost):
    if dp[root]!=-1 and dp[root]>=cost:
        return
    dp[root]=cost
    for p in Path[root]:
        dfs(p,cost+1)

for i in range(1,N+1):
    if Roots[i]==1:
        dfs(i,0)
print(max(dp))

##これはやってることはあってるけど遅くて駄目
# だいたいDPじゃないしね。100倍ぐらい遅いけど答えは出る。