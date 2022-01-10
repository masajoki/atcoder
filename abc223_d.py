#abc223_d
#D - Restricted Permutation 
# https://atcoder.jp/contests/abc223/tasks/abc223_d
# トポロジカルソートと優先度付きキューを使った。

#トポロジカルソート
# 入次数を数えておいて、次数が0のものから取り除いていく。取り除いたら頂点の次数を下げていく
# https://onlinejudge.u-aizu.ac.jp/courses/library/5/GRL/all/GRL_4_B

import heapq
N,M=map(int,input().split())
E=[[] for _ in range (N+1)]
I=[0 for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    E[a].append(b)
    I[b]+=1

queue=[]

for i in range(1,N+1):
    if I[i]==0:
        heapq.heappush(queue,i)

ans=[]

while len(queue)>0:
    v=heapq.heappop(queue)
    ans.append(v)
    for w in E[v]:
        I[w]-=1
        if I[w]==0:
            heapq.heappush(queue,w)
if len(ans)!=N:
    print(-1)
else:
    print(*ans)
