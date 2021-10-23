import bisect
from collections import deque
import heapq
Q=int(input())
Query=[]
A=deque()
Aheap=[]
popped=set()
for i in range(Q):
    q=list(map(int,input().split()))
    Query.append(q)

head=-1
for i in range(Q):
    q=Query[i]
    if q[0]==1:
        x=q[1]
        A.append(x)
    elif q[0]==2:
        if len(Aheap)>0:
            x=heapq.heappop(Aheap)
        else:
            x=A.popleft()
        print(x)
    elif q[0]==3:
        while len(A)>0:
            x=A.popleft()
            heapq.heappush(Aheap,x)
        A.clear()

