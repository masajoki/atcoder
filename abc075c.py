from collections import deque
N,M=map(int,input().split())
AB=[]
path=[[]for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    AB.append((a,b))
    path[a].append(b)
    path[b].append(a)

q=deque()

def solve(skipindex):
    visited=[0 for _ in range(N+1)]
    while len(q)>0:
        island=q.popleft()
        visited[island]=1
        for p in path[island]:
            if (island,p) == AB[i] or (p,island) == AB[i]:
                continue
            elif visited[p]==False:
                q.append(p)
    return sum(visited)

ans=0
for i in range(M):
    q.append(1)
    if solve(i) != N:
        ans+=1
print(ans)


