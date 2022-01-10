#typical90_ac.py
#029 - Long Bricks（★5）
#座標圧縮
#課題2まではこれでいける

import bisect
from collections import defaultdict
W,N=map(int,input().split())
H=[0 for _ in range(N*2+1)]
zahyoSet=set()
zahyo={}

L=[]
R=[]

for i in range(N):
    l,r=map(int,input().split())
    zahyoSet.add((l,i))
    zahyoSet.add((r,i))
    L.append(l)
    R.append(r)

zahyoList=list(zahyoSet)
zahyoList.sort()
for i in range(len(zahyoList)):
    zahyo[zahyoList[i][0]]=i

ans=[]

for i in range(N):
    Li=zahyo[L[i]]
    Ri=zahyo[R[i]]
    height=max(H[Li:Ri+1])+1
    for j in range(Li,Ri+1):
        H[j]=height
    ans.append(height)

for a in ans:
    print(a)