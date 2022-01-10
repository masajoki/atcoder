#typical90_u.py
#021 - Come Back in One Piece（★5） 
#強連結成分(SCC)分解で解く
#2回DFSする。
#最初のDFSは帰りがけに頂点を記録して、トポロジカルソート?する.最後に出現した頂点からもう一度DFSすると
# 強連結していればまた行けるので強連結成分が洗い出せる
# https://hcpc-hokudai.github.io/archive/graph_scc_001.pdf


from collections import defaultdict
import sys
from operator import mul
from functools import reduce

sys.setrecursionlimit(10**7)

#組み合わせの数を計算する関数
def cmb(n,r):
    r = min(n-r,r)
    if r == 0: return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1,r + 1))
    return over // under

N,M=map(int,input().split())
E=[set() for _ in range(N+1)]
revE=[set() for _ in range(N+1)]

revE=[set() for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    E[a].add(b)
    revE[b].add(a)

visited=[ 0 for _ in range(N+1)]
toposorted=[]
def dfs(fromv):
    global renketsu
    visited[fromv]=1
    for v in E[fromv]:
        if visited[v]==0:
            dfs(v)
    toposorted.append(fromv)

for i in range(1,N+1):
    if visited[i]==0:
        dfs(i)

visited=[ 0 for _ in range(N+1)]
SCC=[ [] for _ in range(N+1)]
def dfsrev(fromv,group):
    global renketsu
    global SCC
    visited[fromv]=1
    for v in revE[fromv]:
        if visited[v]==0:
            dfsrev(v,group)
    SCC[group].append(fromv)


for i in toposorted[::-1]:
    if visited[i]==0:
        dfsrev(i,i)

ans=0
for i in range(1,N+1):
    L=len(SCC[i])
    if L>=2:
        t=cmb(L,2)
        ans+=t

print(ans)
