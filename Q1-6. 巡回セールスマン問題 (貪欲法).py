N=int(input())
XY=[]
visited=[0 for _ in range(N+1)]
for i in range(N):
    x,y=map(int,input().split())
    XY.append((x,y))

nowX=XY[0][0]
nowY=XY[0][1]
nextP=0

visited[0]=1
totalDis=0
for _ in range(N-1):
    minDis=10**9
    for i in range(N):
        if visited[i]==0:
            dis=(nowX-XY[i][0])**2 + (nowY-XY[i][1])**2
            if minDis>dis:
                nextP=i
                minDis=min(dis,minDis)
    nowX=XY[nextP][0]
    nowY=XY[nextP][1]
    visited[nextP]=1
    totalDis+=minDis**0.5

totalDis+=((XY[0][0]-nowX)**2 + (XY[0][1]-nowY)**2)**0.5
print(totalDis)
