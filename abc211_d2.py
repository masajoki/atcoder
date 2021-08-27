from collections import deque
N,M=map(int,input().split())
E=[[]for _ in range(N+1)]
count=[0 for _ in range(N+1)]
steps=[float("inf") for _ in range(N+1)]
MOD=10**9+7

count[1]=1
steps[1]=0

for _ in range(M):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)

Q=deque()
Q.append((1,0))

while len(Q) > 0:
    T=Q.popleft()
    tv=T[0]
    ts=T[1]
    for v in E[tv]:
        if steps[v]>steps[tv]+1:
            steps[v]=steps[tv]+1
            count[v]=count[tv]%MOD
            Q.append((v,steps[v]))
        elif steps[v]==steps[tv]+1:
            count[v]+=count[tv]
            count[v]%=MOD

print(count[N])        
        

