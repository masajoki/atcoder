import collections


H,W,C,Q=map(int,input().split())
T=[]
N=[]
colors=[]
for i in range(Q):
    t,n,c=map(int,input().split())
    T.append(t)
    N.append(n)
    colors.append(c)

rowUsed=set()
colUsed=set()
ans=[0 for _ in range(C+1)]
for i in range(Q-1,-1,-1):
    t=T[i]
    n=N[i]
    c=colors[i]
    if t==1: #行を塗る
        if n in rowUsed:
            continue
        else:
            ans[c]+=W-len(colUsed)
            rowUsed.add(n)
    else: #列を塗る
        if n in colUsed:
            continue
        else:
            ans[c]+=H-len(rowUsed)
            colUsed.add(n)
print(*ans[1:])