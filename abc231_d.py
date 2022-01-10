from collections import deque
N,M=map(int,input().split())
E=[0 for _ in range(N+1)]
AB=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    E[a]+=1
    E[b]+=1
    AB[a].append(b)
    AB[b].append(a)



def checkloop():
    queue=deque()
    visited=[0 for _ in range(N+1)]
    for i in range(1,N+1):
        if visited[i]==0:
            queue.append((i,-1))
            while len(queue)>0:
                p,f=queue.popleft()
                visited[p]=1
                for tonari in AB[p]:
                    if visited[tonari]==1:
                        if tonari!=f: #ループしてる
                            return False
                    else:
                        queue.append((tonari,p))
    return True

if max(E)>2:
    print("No")
else:
    if checkloop():
        print("Yes")
    else:
        print("No")
