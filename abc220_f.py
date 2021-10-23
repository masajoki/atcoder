N=int(input())
G=[[] for _ in range(N+1)]

for i in range(N-1):
    u,v=map(int,input().split())
    G[u].append(v)
    G[v].append(u)



for i in range(N):
    ans=0
    
