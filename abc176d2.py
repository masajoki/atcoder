from collections import deque

H,W=map(int,input().split())
start=list(map(int,input().split()))
dest=list(map(int,input().split()))
wall='#'
road='.'
inf=999999999
S=[]
visited=[[ 0 for _ in range(W+1)] for _ in range(H+1)]
magicused=[[ inf for _ in range(W+1)] for _ in range(H+1)]

for i in range(H):
    S.append(list(input()))

queue=deque()

def chkBound(pos):
    h=pos[0]
    w=pos[1]
    if 0<h<=H and  0<w<=W :
        if S[h-1][w-1]!=wall:
            return True
        else:
            return False
    else:
        return False

def walk(pos):
    h=pos[0]
    w=pos[1]
    pathes=[[h-1,w],[h+1,w],[h,w+1],[h,w-1]]
    for p in pathes:
        if chkBound(p):
            h2=p[0]
            w2=p[1]
            magicused[h2][w2]=min(magicused[h][w],magicused[h2][w2])
            if visited[h2][w2]!=1:
                queue.append(p)
                visited[h2][w2]=1

def magic(pos):
    h=pos[0]
    w=pos[1]
    pathes=[]
    for i in [h-2,h-1,0,h+1,h+2]:
        for j in [w-2,w-1,0,w+1,w+2]:
            pathes.append([i,j])
    for p in pathes:
        if chkBound(p):
            h2=p[0]
            w2=p[1]
            magicused[h2][w2]=min(magicused[h][w]+1,magicused[h2][w2])
            if visited[h2][w2]!=1 :
                queue.append(p)
                visited[h2][w2]=1

magicused[start[0]][start[1]]=0
visited[start[0]][start[1]]=1

queue.append(start)
while len(queue) > 0:
    pos=queue.popleft()
    if pos == dest:
        print(magicused[pos[0]][pos[1]])
        exit()
    else:
        walk(pos)
        magic(pos)
print(-1)

