import sys
sys.setrecursionlimit(10**7)
N,M=map(int,input().split())
P=list(map(int,input().split()))
# X,Y=[],[]
Path=[ [] for _ in range(N+1)]
visited=[ False for _ in range(N+1)]
group=[ i for i in range(N+1)]
group2=[ 0 for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    # X.append(x)
    # Y.append(y)
    Path[x].append(y)
    Path[y].append(x)

def dfs(s,g):
    visited[s]=True
    group[s]=g
    for p in Path[s]:
        if visited[p]==False:
            dfs(p,g)

for i in range(1,N+1):
    if visited[i]==False:
        dfs(i,i)

for i in range(N+1):
    group2[P[i-1]]=group[i]


ans=0
for i in range(1,N+1):
    if P[i-1]==i:
        ans+=1
    elif group2[i]==group2[P[i-1]]:
        ans+=1

print(ans)
