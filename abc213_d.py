import sys
sys.setrecursionlimit(10**9)

N=int(input())

Ans=[]
E=[[] for _ in range(N+1)]
Visited=[False for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)

for e in E:
    e.sort()

def dfs(start):
    Visited[start]=True
    print(start,end=" ")
    for v in E[start]:
        if Visited[v]==False:
            dfs(v)
            print(start,end=" ")

dfs(1)
