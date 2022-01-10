#typical90_m.py
#013 - Passing（★5)
#　時間はギリギリだけど正解。ダイクストラを１とNの両方から実行する。
import heapq
from collections import deque
N,M=map(int,input().split())
Edge=[[] for _ in range(N+1)]
Cost={}
for i in range(M):
    a,b,c=map(int,input().split())
    Edge[a].append(b)
    Edge[b].append(a)
    Cost[(a,b)]=c
    Cost[(b,a)]=c

INF=10**10
from1cost=[]
fromNcost=[]
def dijkstra(fromv):
    queue=[]
    count=0
    fromvcost=[INF for _ in range(N+1)]
    heapq.heappush(queue,(0,fromv))
    while len(queue)>0:
        if count==N:
            break
        cost,vertex=heapq.heappop(queue)
        if fromvcost[vertex]==INF:
            fromvcost[vertex]=cost
            count+=1

        for nv in Edge[vertex]:
            if fromvcost[nv]==INF:
                heapq.heappush(queue,(cost+Cost[vertex,nv],nv))
    return fromvcost

from1cost=dijkstra(1)
fromNcost=dijkstra(N)

for i in range(1,N+1):
    print(from1cost[i]+fromNcost[i])



