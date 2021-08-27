#尺取法(もっとかんたんにできそうだけど)
from collections import deque
N,K=map(int,input().split())
A=list(map(int,input().split()))
Ad={}
As=set()
q=deque()
ans=0
for a in A:
    q.append(a)
    if a in Ad.keys():
        Ad[a]+=1
    else:
        Ad[a]=1
    As.add(a)
    if len(As)>K:
        t=q.popleft()
        Ad[t]-=1
        if Ad[t]==0:
            As.remove(t)
    ans=max(len(q),ans)
print(ans)
        