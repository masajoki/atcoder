from collections import deque
H,W,y,x=map(int,input().split())
F=[]
goaly=y-1
goalx=x-1
for i in range(H):
    f=list(map(int,input().split()))
    F.append(f)

degrade=0

Q=deque()

visisted=[[0 for _ in range(W)] for _ in range(H)]
Q.appendleft((0,0,0))
while len(Q)>0:
    y,x,steps=Q.pop()
    if y==goaly and x==goalx:
        print("YES")
        exit()

    visisted[y][x]=1
    
    for h,w in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0<=y+h<H and 0<=x+w<W and visisted[y+h][x+w]==0:
            if F[y+h][x+w]-steps>0:
                Q.appendleft((y+h,x+w,steps+1))

print("NO")