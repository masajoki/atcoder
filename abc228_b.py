from collections import deque
N,X=map(int,input().split())
A=list(map(int,input().split()))
q=deque()
visited=[False] * (N+1)
visited[X]=True
q.append(X)
while len(q)>0:
    f=q.pop()
    visited[f]=True
    nf=A[f-1]
    if visited[nf]==False:
        q.append(nf)

print(visited.count(True))


