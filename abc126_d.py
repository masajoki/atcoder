from collections import deque
import collections
from sys import path_hooks
N=int(input())
color=[-1 for _ in range(N+1)]
U=[]
V=[]
W={}
path=[[] for _ in range(N+1)]
q=deque()
for i in range(N-1):
    u,v,w=map(int,input().split())
    U.append(u)
    V.append(v)
    path[u].append(v)
    path[v].append(u)
    W[(u,v)]=w
    W[(v,u)]=w


for i in range(1,N+1):
    if color[i]==-1:
        q.append((i,0))
    while len(q)>0:
        n_w=q.popleft()
        n,w=n_w
        if w%2==0:
            color[n]=0
        else:
            color[n]=1
        for m in path[n]:
            if color[m]==-1:
                q.append((m,w+W[(n,m)]))

for i in range(1,N+1):
    print(color[i])