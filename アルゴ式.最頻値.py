#アルゴ式.最頻値.py
from collections import defaultdict
N=int(input())
A=list(map(int,input().split()))
C=defaultdict(int)
for a in A:
    C[a]+=1

maxcnt=max(C.values())

Cl=list(C)
ans=[]

for v,c in C.items():
    if c==maxcnt:
        ans.append(v)

ans.sort()
for a in ans:
    print(a)