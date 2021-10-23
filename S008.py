from collections import deque
from copy import deepcopy
H,W=map(int,input().split())
B=[]
INF=10**10
iniCost=[[INF for _ in range(W)] for _ in range(H)]
iniCost[0][0]=0
for i in range(H):
    b=list(input())
    bt=list(map(int,b))
    B.append(bt)

saikoro=(1,2,5,4,3,6) # 天面0,上1,下2,左3,右4,底面5)
def ue(s):
    return (s[2],s[0],s[5],s[3],s[4],s[1])

def sita(s):
    return (s[1],s[5],s[0],s[3],s[4],s[2])

def migi(s):
    return (s[3],s[1],s[2],s[5],s[0],s[4])

def hidari(s):
    return (s[4],s[1],s[2],s[0],s[5],s[3])

Q=deque()
Q.append((0,0,saikoro,iniCost))
ans=INF
while len(Q)>0:
    y,x,sai,Cost=Q.pop()
    ans=min(Cost[H-1][W-1],ans)
    #ue
    if 0<=y-1<H:
        newsai=ue(sai)
        newcost=abs(B[y-1][x]-newsai[0])+Cost[y][x]
        nowCost=Cost[y-1][x]
        if nowCost>newcost and  ans>newcost:
            cost=deepcopy(Cost)
            cost[y-1][x]=newcost
            Q.append((y-1,x,newsai,cost))
    # sita
    if 0<=y+1<H:
        newsai=sita(sai)
        newcost=abs(B[y+1][x]-newsai[0])+Cost[y][x]
        nowCost=Cost[y+1][x]
        if nowCost>newcost  and ans>newcost:
            cost=deepcopy(Cost)
            cost[y+1][x]=newcost
            Q.append((y+1,x,newsai,cost))

    # migi
    if 0<=x+1<W:
        newsai=migi(sai)
        newcost=abs(B[y][x+1]-newsai[0])+Cost[y][x]
        nowCost=Cost[y][x+1]
        if nowCost>newcost and ans>newcost:
            cost=deepcopy(Cost)
            cost[y][x+1]=newcost
            Q.append((y,x+1,newsai,cost))

    # hidari    
    if 0<=x-1<W:
        newsai=hidari(sai)
        newcost=abs(B[y][x-1]-newsai[0])+Cost[y][x]
        nowCost=Cost[y][x-1]
        if nowCost>newcost:
            cost=deepcopy(Cost)
            cost[y][x-1]=newcost
            Q.append((y,x-1,newsai,cost))
print(ans)
pass    

