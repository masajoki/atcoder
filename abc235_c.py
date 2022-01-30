#abc235_c.py
from collections import defaultdict
N,Qn=map(int,input().split())
Q=[]
A=list(map(int,input().split()))
for i in range(Qn):
    x,k=map(int,input().split())
    Q.append((x,k))

counter=defaultdict(int)
position={}

for i in range(N):
    counter[A[i]]+=1
    position[(A[i],counter[A[i]])]=i

for x,k in Q:
    if (x,k) in position:
        print(position[(x,k)]+1)
    else:
        print(-1)