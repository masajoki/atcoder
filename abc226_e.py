from collections import deque
N,M=map(int,input().split())
G=[[] for _ in range(N+1)]

for i in range(M):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)

candidate=0
visited=[0 for _ in range(N+1)]
for i in range(1,N+1):
    q=deque()
    if visited[i]==0:
        q.append(i)
    else:
        continue
    guusuu=0
    ichi=0
    san=0
    while len(q)>0:
        v=q.popleft()
        visited[v]=1
        if len(G[v])==2:
            guusuu+=1
        elif len(G[v]) ==1:
            ichi+=1
        elif len(G[v]) ==3:
            san+=1
        else:
            print(0)
            exit()

        for u in G[v]:
            if visited[u]==0:
                q.append(u)
    if ichi==1 and san==1 and guusuu>1 :
        candidate+=1
    elif ichi==0 and san==0 and guusuu>1:
        candidate+=1
    else:
        print(0)
        exit()

print(pow(2,candidate,998244353))