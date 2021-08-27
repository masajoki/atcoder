#ダイクストラだった。
#ごちゃごちゃやってるのは高速化を狙って。600msecぐらいでギリギリ。
#一度path[a][b]のような持ち方にしたら遅くなった。１０＊＊５ｘ１０＊＊５になるからそりゃそうかと思う。

import heapq
N,M,X,Y=map(int,input().split())
A=[]
B=[]
T=[]
K=[]
path=[set() for _ in range(N+1)]
for i in range(M):
    a,b,t,k=map(int,input().split())
    path[a].add((b,t,k))
    path[b].add((a,t,k))

cost=[10**30 for i in range(N+1)]
cost[X]=0
visited=[False for _ in range(N+1)]
queue=[(0,X)]
while queue:

    msg=heapq.heappop(queue)
    curstation=msg[1]
    curcost=msg[0]
    if visited[curstation]:
        continue
    else:
        visited[curstation]=True
    for p in path[curstation]:
        b=p[0]
        t=p[1]
        k=p[2]
        if visited[b]==False:
            tempcost=cost[b]
            if curcost%k==0:
                newcost=curcost+t
            else:
                newcost=curcost+t+(k-curcost%k)
            if tempcost>newcost:
                cost[b]=newcost
                heapq.heappush(queue,(newcost,b))

if visited.count(True)==N:
    print(cost[Y])
else:
    print(-1)
