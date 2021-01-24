from collections import deque
H,W=map(int,input().split())
S=[]
for i in range(H):
    s=list(input())
    S.append(s)

maxStep=[[-1 for _ in range(W)] for _ in range(H)]

def searchmaze(starth,startw):
    startpoint=[starth,startw,0] #w,h,steps
    visited=[[0 for _ in range(W)] for _ in range(H)]
    q=deque()
    q.append(startpoint)
    while len(q)>0:
        p=q.popleft()
        h=p[0]
        w=p[1]
        step=p[2]
        if S[h][w]=='.' and visited[h][w]==0:
            maxStep[h][w]=max(step,maxStep[h][w])
            visited[h][w]=1
            for nextp in [[-1,0],[0,-1],[1,0],[0,1]]:
                nexth=p[0]+nextp[0]
                nextw=p[1]+nextp[1]
                if 0 <= nexth < H and 0 <= nextw < W:
                    q.append([nexth,nextw,step+1]) 

for h in range(H):
    for w in range(W):
        if S[h][w]==".":
            searchmaze(h,w)

maxsteps=0
for h in range(H):
    for w in range(W):
        maxsteps=max(maxStep[h][w],maxsteps)
print(maxsteps)