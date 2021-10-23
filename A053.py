from collections import deque
H,W=map(int,input().split())
visited=[[0 for _ in range(W)] for _ in range(H)]

Q=deque()
S=[]
for i in range(H):
    s=input()
    S.append(s)


count=0
strokes={}
strokes['G']=0
strokes['R']=0
strokes['B']=0

for h in range(H):
    for w in range(W):
        if visited[h][w]==0:
            color=S[h][w]
            Q.append((h,w,color))
            strokes[color]+=1
            while len(Q)>0:
                y,x,color=Q.pop()
                visited[y][x]=1
                for yp,xp in ((1,0),(0,1),(-1,0),(0,-1)):
                    yt=y+yp
                    xt=x+xp
                    if 0<=xt<W and 0<=yt<H and S[yt][xt]==color:
                        if visited[yt][xt]==0:
                            Q.append((yt,xt,color))
            
print(strokes['R'],strokes['G'],strokes['B'])