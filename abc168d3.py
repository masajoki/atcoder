import sys
from collections import deque
sys.setrecursionlimit(10**7)

N,M=map(int,input().split())
PATH=[[] for _ in range(N+10)]
sign=[-1 for _ in range(N+10)]
steps=[999999999 for _ in range(N+10)]
for i in range(M):
    a,b=map(int,input().split())
    PATH[a].append(b)
    PATH[b].append(a)

#幅優先探索
dq=deque()
dq.append([0,1,0])
while len(dq)>0:
    last,current,step=dq.popleft()
    if steps[current]>step :
        steps[current] = step
        sign[current]=last
    
        for nextroom in PATH[current]:
            if steps[nextroom]>step : #これ2回比較して無駄臭い
                dq.append([current,nextroom,step+1])

#絶対に最短経路はみつかる
print("Yes")

for i in range(2,N+1):
    print(sign[i])
