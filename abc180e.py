N=int(input())
POS=[]
visited=[]
disFromPos1=0


for _ in range(N):
    X,Y,Z=map(int,input().split())
    POS.append([X,Y,Z])

totalcost=0
nearestcost=10**7
nearestpos=0
lastpos=POS[0]
for _ in range(N):
    for i in range(1,N):
        p=POS[i]
        cost=abs(p[0]-lastpos[0])+abs(p[1]-lastpos[1])+max(0,p[2]-lastpos[2])
        if nearestcost > cost and i not in visited:
            nearestcost=cost
            nearestpos=i
    visited.append(nearestpos)
    totalcost+=nearestcost
    lastpos=POS[nearestpos]

p=POS[0]
totalcost+=abs(p[0]-lastpos[0])+abs(p[1]-lastpos[1])+max(0,p[2]-lastpos[2])
print(totalcost)


