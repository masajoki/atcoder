from collections import deque
# import heapq
N,M=map(int,input().split())
pathes=[ [] for _ in range(N+1)] 
sign=[]  #cost[移動元部屋番号]=移動先部屋番号 
# cost=[ 999999 for _ in range(N)] for i in range(1,N+1)] #cost[スタート部屋番号][到達部屋番号] 
routes=[[] for _ in range(N+1)]


for i in range(M):
    a,b=map(int,input().split())
    pathes[a].append(b)
    pathes[b].append(a)




for i in range(2,N+1):
    visited=[False for _ in range(N+1)]
    route=[]
    route.append(i)
    bfsq=deque()
    bfsq.append([i,route])
    # visited[i]=True
    while len(bfsq)>0:
        job=bfsq.popleft()
        if job[0]==1:
            route=job[1]
            route.append(1)
            routes.append(route)
            continue
        for path in pathes[job[0]]:
            posi=job[0]
            route=job[1]
            if visited[posi]==False:
                visited[posi]=True
                route.append(path)
                bfsq.append([posi,route.copy()])

pass


    
