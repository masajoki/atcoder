from collections import deque

N,M=map(int,input().split())
E=[[] for _ in range(N+1)]
Q=deque()
for i in range(M):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)

count=[0 for _ in range(N+1)] 
step=[float("inf") for _ in range(N+1)]

MOD=10**9+7

ans=0
minstep=10**5*2+1

Goal=False
visited=[False for _ in range(N+1)]
visited[1]=True
Q.append((1,0))
count[1]=1
while len(Q)>0:
    t=Q.popleft()
    tempv=t[0]
    tempstep=t[1]
    visited[tempv]=True

    if tempstep+1 > minstep:
        continue
    for v in E[tempv]:
        if v==N:
            if Goal==False:
                step[N]=tempstep+1
                minstep=step[N]
                count[N]+=count[tempv]
                Goal=True
            elif tempstep+1==step[N]:
                count[N]+=count[tempv]
        elif visited[v]==True:
            if step[v]>tempstep+1:
                step[v]=tempstep+1
                count[v]=count[tempv]
            elif step[v]==tempstep+1:
                count[v]+=count[tempv]
        elif visited[v]==False:
            step[v]=tempstep+1
            count[v]=count[tempv]
            Q.append((v,tempstep+1))

print(count[N]%MOD)
