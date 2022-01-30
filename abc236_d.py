#abc236_d.py
from itertools import combinations
N=int(input())
A=[[-1 for _ in range(2*N+1)] for _ in range(2*N+1)]

for i in range(1,2*N):
    T=list(map(int,input().split()))
    for j in range(i+1,2*N+1):
        A[i][j]=T[j-i-1]


from collections import deque
from copy import deepcopy

queue=deque()
visitedset={}

for i in range(1,2*N+1):
    a=A[1][i]
    if a!=-1:
        visited=[-1 for _ in range(2*N+1)]
        visited[1]=1
        visited[i]=1
        queue.append((visited,a))
        visitedset[visited]=a

ans=0
while len(queue)>0:
    visited,a=queue.popleft()
    if visited.count(-1)==1:
        ans=max(a,ans)

    for i in range(1,2*N):
        if visited[i]==-1:
            visited[i]=1
            for j in range(i+1,2*N+1):
                if visited[j]==-1:
                    b=A[i][j]
                    if b!=-1:
                        c=a^b
                        visited2=deepcopy(visited)
                        visited2[j]=1
                        queue.append((visited2,c))

print(ans)