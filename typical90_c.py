#幅優先探索を2回やればよい
from collections import deque
N=int(input())
E=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)





def dfs(startCity):
    maxsteps=0
    farthestCity=-1
    visited=[ False for _ in range(N+1)]
    q=deque()
    q.append((startCity,maxsteps))
    while len(q)>0:
        t=q.popleft()
        city=t[0]
        steps=t[1]
        visited[city]=True
        for v in E[city]:
            if visited[v]==False:
                q.append((v,steps+1))
                if maxsteps<(steps+1):
                    maxsteps=steps+1
                    farthestCity=v
    return farthestCity,maxsteps

farthestCity,maxsteps=dfs(1)
_,maxsteps=dfs(farthestCity)
print(maxsteps+1)


