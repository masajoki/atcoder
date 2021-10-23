from collections import deque
H,W=map(int,input().split())
S=[]
startH=-1
startW=-1
for i in range(H):
    s=input()
    if 'S' in s:
        startW=s.index("S")
        startH=i
    S.append(s)

visited=[[0 for _ in range(W)]for _ in range(H)]
Q=deque()
Q.append((startH,startW))
while len(Q)>0:
    y,x=Q.pop()
    visited[y][x]=1
    
    for h,w in ((1,0),(-1,0),(0,1),(0,-1)):
        if 0<=y+h<H and 0<=x+w<W and visited[y+h][x+w]==0:
            if S[y+h][x+w] =='.':
                Q.append((y+h,x+w))
        elif y+h<0 or x+w<0 or x+w>=W or y+h>=H:
            print("YES")
            exit()


print("NO")






