import sys
sys.setrecursionlimit(10**7)

N=int(input())
C=list(map(int,input().split()))

Clist= [0 for _ in range(max(C)+1)]

AB=[ [] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)


Good=[False for _ in range(N+1)]
Good[1]=True

visited=[False for _ in range(N+1)]

def dfs(v):
    visited[v]=True
    if Clist[C[v-1]]==0:
        Good[v]=True
    Clist[C[v-1]]+=1
    for v2 in AB[v]:
        if visited[v2]==False:
            dfs(v2)
    Clist[C[v-1]]-=1

v=1
Clist[C[v-1]]=1
dfs(v)

for i in range(len(Good)):
    if Good[i]==True:
        print(i)