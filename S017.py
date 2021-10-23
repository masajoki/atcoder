from collections import deque
from typing import Counter
ansQ=[]
N,M,S=map(int,input().split())
T=[]
Mapper=[[] for _ in range(S+1)]
Count=[[i,0] for i in range(S+1)]
for i in range(N):
    s=input()
    T.append(s)
    for j in range(N):
        st=s[j]
        for k in range(S):
            if st==str(k):
                Count[k][1]+=1
                Mapper[k].append((i,j))

Count.sort(key=lambda x: x[1],reverse=True)


for c in Counter:
    s,cnt=c
    if s==0:
        continue

