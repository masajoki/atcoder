from collections import deque
N=int(input())
PATH=[[] for _ in range(N+1)]
A=[]
B=[]
C=[0 for _ in range(N+1)]
T=[]
E=[]
X=[]
seibun=[0 for _ in range(N+1)]
vertForSeibun=[set() for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    PATH[a].append(b)
    PATH[b].append(a)

Q=int(input())

queue=deque()


# for i in range(Q):
#     t,e,x=map(int,input().split())
#     T.append(t)
#     E.append(e)
#     X.append(x)

curseibun=1
for i in range(1,N+1):
    if seibun[i]==0:
        queue.append(i)
        seibun[i]=curseibun
        vertForSeibun[curseibun].add(i)

    while len(queue)> 0:
        vertex=queue.popleft()
        seibun[vertex]=curseibun
        vertForSeibun[curseibun].add(vertex)
        
        for path in PATH[vertex]:
            if seibun[path]==0:
                queue.append(path)
    curseibun+=1

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
    s=seibun[startp]
    vertexes=vertForSeibun[s]
    for v in vertexes:
        if v==avoidp:
            continue
        C[v]+=x

for i in range(1,len(C)):
    print(C[i])






