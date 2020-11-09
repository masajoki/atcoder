Hmin=0
Hmax=420
Wmin=0
Wmax=420
padY=Hmax//2
padX=Wmax//2
#0 : 未訪問
#1 : 訪問済み
#-1 : ゴール  
#-2 : 壁

queue=[]
dYX=[[1,1],[1,0],[1,-1],[0,1],[0,-1],[-1,0]] #金の動き
C=list([0]*Hmax for _ in range(Wmax))

N,X,Y=map(int,input().split())

for _ in range(N):
    x,y=map(int,input().split())
    C[y+padY][x+padX]=-2
C[Y+padY][X+padX]=-1

currentX=0+padX
currentY=0+padY

queue.append([currentY,currentX])

while len(queue)>0:
    pos=queue.pop(0)
    currentY,currentX=pos

    if Hmin < currentY < Hmax and Wmin < currentX < Wmax:
        for d in dYX:
            nextY,nextX=currentY+d[0],currentX+d[1]
            if C[nextY][nextX]==-1:#goal
                print (C[currentY][currentX]+1) 
                exit()
            elif C[nextY][nextX]==0:
                C[nextY][nextX]=C[currentY][currentX]+1 #経路数
                queue.append([nextY,nextX])
            elif C[nextY][nextX]==-2:
                continue
print(-1) 
