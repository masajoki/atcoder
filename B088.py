from collections import deque
H,W=map(int,input().split())
Q=deque()
S=[]
for i in range(H):
    s=input()
    S.append(s)

visited=[[0 for _ in range(W)]for _ in range(H)]

Q.append((0,0,(1,0))) #x,y,d(x,y):向き
while len(Q)>0:
    x,y,d=Q.popleft()
    visited[y][x]=1
    dL=(d[1],-d[0])
    dR=(-d[1],d[0])
    if 0<=y+d[1]<H and 0<=x+d[0]<W: #枠内
        if S[y+d[1]][x+d[0]]=='.' and visited[y+d[1]][x+d[0]]==0: #進行方向
            Q.append((x+d[0],y+d[1],(d[0],d[1])))
            continue
    if 0<=y+dR[1]<H and 0<=x+dR[0]<W: #右
        if S[y+dR[1]][x+dR[0]]=='.' and visited[y+dR[1]][x+dR[0]]==0: #進行方向
            Q.append((x+dR[0],y+dR[1],(dR[0],dR[1])))
            continue
    if 0<=y+dL[1]<H and 0<=x+dL[0]<W: #左
        if S[y+dL[1]][x+dL[0]]=='.' and visited[y+dL[1]][x+dL[0]]==0: #進行方向
            Q.append((x+dL[0],y+dL[1],(dL[0],dL[1])))
            continue
print(x,y)