#072 - Loop Railway Plan（★4）
#典型90問
# 回答は再帰でとのことだが、BFSでも行ける。
from collections import deque
from copy import deepcopy
H,W=map(int,input().split())

queue=deque()
template=[]
for i in range(H):
    t=list(input())
    template=template+t

maxsteps=0
for i in range(H):
    for j in range(W):
        if template[i*W+j]=='.':
            visited=[-1]*(H*W)
            visited[i*W+j]=2
            queue.append([i,j,visited,0])
            while len(queue)>0:
                h,w,visited,steps=queue.popleft()
                for (h2,w2) in ((h+1,w),(h-1,w),(h,w-1),(h,w+1)):
                    if 0<=h2<H and 0<=w2<W:
                        if visited[h2*W+w2]==2:
                            maxsteps=max(steps+1,maxsteps)
                        elif template[h2*W+w2]=='.' and visited[h2*W+w2] ==-1:
                            visited2=deepcopy(visited)
                            visited2[h2*W+w2]=1
                            queue.append((h2,w2,visited2,steps+1))
if maxsteps<=3:
    maxsteps=-1
print(maxsteps)
