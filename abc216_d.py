import heapq
from collections import deque
N,M=map(int,input().split())
K=[]
A=[]
AQ=[]
Ball=[]
possible=True
for i in range(M):
    k=int(input())
    a=list(map(int,input().split()))
    q=deque()
    K.append(k)
    # A.append(a)
    dpucheck=set()
    for j in range(k):
        q.append(a[j])
        dpucheck.add(a[j])
    AQ.append(q)
    if len(dpucheck)!=k:
        possible=False

if possible==False:
    print("No")
    exit()

tempq=deque()

temparea=[0 for _ in range(N+1)]
rememberq=[[] for _ in range(N+1)]
inflightq= [ False for _ in range(M+1)]

doneball=[]

queofque=deque()
for i in range(M):
    queofque.append(i)
while True:
    if len(doneball)==N:
        print("Yes")
        exit()
    tumi=True
    while len(queofque)>0:
        i=queofque.pop()
        if len(AQ[i])>0 and inflightq[i]==False:
            q=AQ[i]
            a=q.pop()
            inflightq[i]=True
            temparea[a]+=1
            rememberq[a].append(i)

        if temparea[a]==2:
            doneball.append(a)
            q1,q2=rememberq[a]
            inflightq[q1]=False
            inflightq[q2]=False
            queofque.append(q1)
            queofque.append(q2)
            tumi=False
            temparea[a]=-1
    if tumi==False:
        tumi=True
    else:
        print("No")
        exit()