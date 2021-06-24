N=int(input())
Pt=list(map(int,input().split()))
Q=int(input())
PATH=[ set() for _ in range(N+1)]
P=[-1 for _ in range(N+1)]
for i in range(2,N+1):
    P[i]=Pt[i-2]

for i in range(2,N+1):
    PATH[i].add(P[i])
    PATH[P[i]].add(i)




U=[]
D=[]
for i in range(Q):
    u,d=map(int,input().split())
    U.append(u)
    D.append(d)

Distance=[-1 for _ in range(N+1)]

for i in range(1,N+1):
    if i == P[i]:
        Distance[i]=0

def dfs(s,distance):
    for p in PATH[s]:
        if Distance[p]==-1:
            Distance[p]=distance+1
            dfs(p,distance+1)

dfs(1,0)

for i in range(Q):
    