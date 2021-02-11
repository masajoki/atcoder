from collections import deque
import copy

N,M=map(int,input().split())
Path=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    Path[a].append(b)

K=int(input())
C=list(map(int,input().split()))



Q=deque()
Visited=[0 for _ in range(N+1)]
Visited[C[0]]=1
startpoint=[C[0],Visited,1]
Q.append(startpoint)
CVisited=[0 for _ in range(N+1)]
Cdict={}
for c in C:
    Cdict[c]=0

while len(Q) > 0:
    msg=Q.popleft()
    stone=msg[0]
    Visited=msg[1]
    steps=msg[2]
    Visited[stone]=1
    for p in Path[msg[0]]:
        if p in C:
            C.remove(p)
            Cdict[p]=1
            Visited=[0 for _ in range(N+1)]
            for k in Cdict.keys():
                if Cdict[k]==1:
                    Visited[k]=1

        if Visited[p]!=1:
            t=[p,copy.deepcopy(Visited),steps+1]
            Q.append(t)
    allStoneDone=True
    for c in C:
        if Visited[c]==0:
            allStoneDone=False
    if allStoneDone:
        print(steps)
        exit()

print(-1)

            
    
    
