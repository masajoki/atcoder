import sys
from collections import deque
from copy import deepcopy
sys.setrecursionlimit(10**7)

N=int(input())
C=list(map(int,input().split()))

Clist= [[False for _ in range(max(C)+1)] for _ in range(N+1)]

AB=[ [] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)


Good=[0 for _ in range(N+1)]
Good[1]=1

Q=deque()
visited=[False for _ in range(N+1)]
# Clist=set()
# Clist.add(C[1-1])

def selfcopy(A):
    B=[]
    for a in A:
        B.append

Clist[C[0]]=True
Q.append([1,Clist])

while len(Q)>0:
    v,Clist=Q.popleft()
    visited[v]=True
    for p in AB[v]:
        if visited[p]==False:
            if Clist[C[p-1]]==False:
                Good[p]=1
            Ctemp=deepcopy(Clist)
            Ctemp[C[p-1]]=True
            Q.append([p,Ctemp])

for i in range(len(Good)):
    if Good[i]==1:
        print(i)