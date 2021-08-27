#なんでWAになるのかわからんけど、1次元にすると整数倍早くなるということは学んだ。
#0-1BFSで
from collections import deque
H,W=map(int,input().split())
ys,xs=map(int,input().split())
yt,xt=map(int,input().split())
ys-=1
yt-=1
xs-=1
xt-=1

S=""

for i in range(H):
    S=S+input()

rotated=[ float("inf") for _ in range ((W) * (H))]
rotated[ys*W+xs]=0

Q=deque()
Q.append((ys,xs,0,0))#直前に動いた方向(v,h) 



while len(Q)>0:
    y,x,vp,hp=Q.popleft()
    prepos=y*W+x
    print(y,x,vp,hp,rotated[prepos])

    if y==yt and x==xt:
        print(rotated[yt*W+xt]-1)
        exit()
    
    for v,h in ((-1,0),(1,0),(0,-1),(0,1)):
        nextpos=(y+v)*W+x+h
        if H>(y+v)>=0 and W>(x+h)>=0 and S[nextpos]=="." :
            change=1
            if v==vp and h==hp:
                change=0
                Q.appendleft((y+v,x+h,v,h))
            else:
                Q.append((y+v,x+h,v,h))
            rotated[nextpos]=min(rotated[nextpos],rotated[prepos]+change)

            if change==0 and visited[nextpos]==False:
                Q.appendleft((y+v,x+h,v,h))
            elif visited[nextpos]==False:
                Q.append((y+v,x+h,v,h))
