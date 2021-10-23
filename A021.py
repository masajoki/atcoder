from collections import deque
H,W=map(int,input().split())
S=[]
S.append('.'*(W+2))
for i in range(H):
    s=input()
    s='.'+s+'.'
    S.append(s)
S.append('.'*(W+2))

H=H+2
W=W+2

visited=[[0 for _ in range(W)] for _ in range(H)]



ans=[]
islands=0
area=[0 for _ in range(100*100+1)]
length=[0 for _ in range(100*100+1)]

def bfs(y,x):
    global islands
    global area
    global length
    Q=deque()
    if visited[y][x]==0:
        #上陸
        islands+=1
        length[islands]=0
        area[islands]=0
    else:
        return

    Q.append((y,x)) #x,y,面積,海岸線
    visited[y][x]=islands
    while len(Q)>0:
        y,x=Q.pop()
        area[islands]+=1
        for h,w in ( (1,0),(-1,0),(0,1),(0,-1) ):
            if S[h+y][w+x]=='.':
                length[islands]+=1
            if S[h+y][w+x]=='#' and visited[h+y][w+x]==0:
                Q.append((y+h,x+w))
                visited[y+h][x+w]=islands


    
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            bfs(i,j)


arealength=[]
for i in range(len(area)):
    if area[i]!=0:
        arealength.append((area[i],length[i]))

arealength.sort(reverse=True)


for a,l in arealength:
    print(a,l)




