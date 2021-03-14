#愚直に実装して間に合わないバージョン
from collections import deque
N=int(input())
PATH=[[] for _ in range(N+1)]
A=[]
B=[]
C=[0 for _ in range(N+1)]
T=[]
E=[]
X=[]
for i in range(N-1):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    PATH[a].append(b)
    PATH[b].append(a)

Q=int(input())

queue=deque()

for i in range(Q):
    t,e,x=map(int,input().split())
    startp=0
    avoidp=0
    if t==1:
        startp=A[e-1]
        avoidp=B[e-1]
    else:
        startp=B[e-1]
        avoidp=A[e-1]
    queue.append(startp)
    visited=[False for _ in range(N+1)]
    while len(queue)>0:
        point=queue.popleft()
        C[point]+=x
        visited[point]=True
        for p in PATH[point]:
            if p != avoidp and visited[p]==False:
                queue.append(p)

for i in range(1,len(C)):
    print(C[i])