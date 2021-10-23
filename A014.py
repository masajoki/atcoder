import collections
from sys import version_info 
H,W,N=map(int,input().split())
C=[]
fA=[]
fB=[]
tA=[]
tB=[]
C.append('.'*(W+2))

for i in range(H):
    s=input()
    s=". "+s+" ."
    C.append(list(s.split()))
C.append('.'*(W+2))

for i in range(N):
    fa,fb,ta,tb=map(int,input().split())
    fA.append(fa)
    fB.append(fb)
    tA.append(ta)
    tB.append(tb)


def search(y,x,ty,tx):
    if C[y][x]!=C[ty][tx]:
        return False

    visited=[[0 for _ in range(W+2)]for _ in range(H+2)]
    Q=collections.deque()
    Q.append((y,x,(0,0),-1))
    startc=C[y][x]


    while len(Q)>0:
        y,x,d,b=Q.popleft()
        visited[y][x]=1
        if b!=-1 and C[y][x]==startc and y==ty and x==tx:
            return True
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny=y+dy
            nx=x+dx
            if 0<=ny<H+2 and 0<=nx<W+2:
                pass
            else:
                continue 
            tb=b
            if d[0]==dy and d[1]==dx:
                pass
            else:
                tb=b+1
            if tb<=2:
                if (C[ny][nx]=='.' or C[ny][nx]==startc )and visited[ny][nx]==0:
                    Q.append((ny,nx,(dy,dx),tb))
    return False
            

for i in range(N):
    if search(fA[i],fB[i],tA[i],tB[i]):
        print("yes")
    else:
        print("no")    


