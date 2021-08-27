#適当なところからDFSして、偶数番目または奇数番目の頂点をn//2こならべればよい

from collections import deque
N=int(input())
E=[[]for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    E[a].append(b)
    E[b].append(a)

Q=deque()
Q.append((1,0))
T=[[] for _ in range(N+1)]
Visited=[False for _ in range(N+1)]

while len(Q)>0:
    v,cnt=Q.popleft()
    Visited[v]=True
    cnt+=1
    for e in E[v]:
        if Visited[e]==False:
            T[cnt].append(e)
            Q.append((e,cnt))

cnt=0
for i in range(len(T)):
    if i%2==0:
        cnt+=len(T[i])
d=0
if cnt<N//2:
    d=1

counter=0
for i in range(len(T)):
    if i%2==d:
        for t in T[i]:
            if counter!=N//2:
                print(t,end=" ")
                counter+=1
            else:
                exit()


