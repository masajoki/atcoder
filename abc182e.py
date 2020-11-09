from collections import deque

H,W,n,m=map(int,input().split())
A=[]
B=[]
C=[]
D=[]
for _ in range(n):
    a,b=map(int,input().split())
    A.append(a-1)
    B.append(b-1)
for _ in range(m):
    a,b=map(int,input().split())
    C.append(a-1)
    D.append(b-1)

masu=[]
for h in range(H):
    masu=[[0]*W for i in range(H)]

for i in range(m):
    masu[C[i]][D[i]]=-1

def bfs (sy,sx,startnum):
    posiq=deque([[sy,sx]]
    )
    while posiq:
        y,x=posiq.popleft()
        if y+1<=H-1:
            p=masu[y+1][x]
            if p>=0 and p<startnum:
                masu[y+1][x]=startnum
                posiq.append([y+1, x])
        if y-1>=0:
            p=masu[y-1][x]
            if p>=0 and p<startnum:
                masu[y-1][x]=startnum
                posiq.append([y-1, x])
        if x+1<=W-1:
            p=masu[y][x+1]
            if p>=0 and p<startnum:
                masu[y][x+1]=startnum
                posiq.append([y, x+1])
        if x-1>=0:
            p=masu[y][x-1]
            if p>=0 and p<startnum:
                masu[y][x-1]=startnum
                posiq.append([y, x-1])

for i in range(n):
    masu[A[i]][B[i]]=i+1
    bfs(A[i],B[i],i+1)

print(0)

##これじゃだめだった！！！向きが拡散しちゃだめだった。
