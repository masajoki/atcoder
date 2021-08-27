from collections import deque
N,M=map(int,input().split())
AB=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    AB[a].append(b)

ans=0
q=deque()
for i in range(1,N+1):
    visited=[0 for _ in range(N+1)]
    visited[i]=i
    q.append(i)

    while len(q)>0:
        a=q.popleft()
        for b in AB[a]:
            if visited[b]!=i:
                q.append(b)
                visited[b]=i
    
    ans+=visited.count(i)
    

print(ans)        




