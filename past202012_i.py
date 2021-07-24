#回答見てAC
# 最初はDFSでやろうとしたがうまく行かず。
# 次にbfsでやろうとしたがうまく行かず。
# ゴール起点のBFSでやったら自然に記述でき、うまく行った。

from collections import deque
N,M,K=map(int,input().split())
H=list(map(int,input().split()))
C=list(map(int,input().split()))
isC=[ [] for _ in range(N+1)]
for c in C:
    isC[c]=True

q=deque()

Path=[ [] for _ in range(N+1)] #逆向きに作る
Step=[ float('inf') for _ in range(N+1)]
for c in C:
    Step[c]=0
for i in range(M):
    a,b=map(int,input().split())
    if H[a-1]<H[b-1]:
        Path[a].append(b)
    else:
        Path[b].append(a)

for i in C:
    for p in Path[i]:
        q.append((p,1))

    while len(q)>0:
        city,step=q.popleft()
        if step < Step[city]:
            Step[city]=step
            for np in Path[city]:
                q.append((np,step+1))

for i in range(1,N+1):
    if Step[i]==float('inf'):
        print(-1)
    else:
        print(Step[i])
 

