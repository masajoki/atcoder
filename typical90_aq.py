#typical90_aq.py
#043 - Maze Challenge with Lack of Sleep（★4）
#0-1BFS で溶けるらしい
from collections import deque
H,W=map(int,input().split())
dp=[[10**8 for _ in range(4) ] for _ in range(W*H)]
rs,cs=map(int,input().split())
rt,ct=map(int,input().split())
rs-=1
rt-=1
cs-=1
ct-=1
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

S=[]
for i in range(H):
    s=list(input())
    S=S+s

queue=deque()
queue.append((rs,cs,-1,0)) #ypos,xpos,向き,向きを変えた数

while len(queue)>0:
    y,x,prevdir,turns=queue.popleft()
    if prevdir!=-1 and dp[rt*W+ct][prevdir]<turns:
        continue
    if y==rt and x==ct:
        break

    for d in range(4):
        dir=directions[d]
        h=y+dir[0]
        w=x+dir[1]
        if 0<=h<H and 0<=w<W:
            turn=0
            if prevdir != d and prevdir!=-1:
                turn=1
            if S[h*W+w]=='.' and dp[h*W+w][d] > turns+turn:
                dp[h*W+w][d]=turns+turn
                if turn ==1:
                    queue.append((h,w,d,turns+turn))
                else:
                    queue.appendleft((h,w,d,turns))
print(min(dp[rt*W+ct]))
