from collections import deque
import copy
H,W=map(int,input().split())
S=[]
roadCounts=0

for i in range(H):
    s=list(input())
    S.append(s)
    roadCounts+=s.count('.')
    
Q=deque() #[start,path] を入れる 
start=[0,0]
path=[] #現在地点までのパスを入れていく
Q.append([start,path])
while len(Q)>0:
    m=Q.popleft()
    pos,path=m
    y,x=pos
    if x==W-1 and y==H-1:
        path.append([H-1,W-1])
        break
    if S[y][x]=='#':
        continue
    else:
        S[y][x]='#' #訪問済み

    for move in [[1,0],[-1,0],[0,1],[0,-1]]:
        mY,mX=move
        if 0<=y+mY<H and 0<=x+mX<W:
            nextpos=[y+mY,x+mX]
            nextpath=copy.deepcopy(path)
            nextpath.append([y,x])
            Q.append([nextpos,nextpath])

lastY,lastX=path[-1]
if lastY==H-1 and lastX==W-1:
    print(roadCounts-len(path))
else:
    print(-1)