N,M,Q=map(int,input().split())
graph=[[] for _ in range(N+1)] #配列の配列初期化
for i in range(M):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
temp=list(map(int,input().split()))
color=[0]*(N+1)
for i in range(1,N+1):
    color[i]=temp[i-1] #kuso code

for i in range(Q):
    s=list(map(int,input().split()))
    if s[0]==1:
        print(color[s[1]])
        for n in graph[s[1]]:
            color[n]=color[s[1]]    
    else:
        print(color[s[1]])
        color[s[1]]=s[2]    
