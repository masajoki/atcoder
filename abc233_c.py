#abc233_c
# BFSっぽくなってしまったが、DFSのほうが簡単そう
from collections import deque
N,X=map(int,input().split())
A=[]
L=[]
for i in range(N):
    T=list(map(int,input().split()))
    L.append(T[0])
    A.append(T[1:])

Q=deque(A[0])

for i in range(1,N):
    for j in range(len(Q)):
        t=Q.popleft()
        for a in A[i]:
            Q.append(t*a)

ans=0
for t in Q:
    if t==X:
        ans+=1
print(ans)