N,M=map(int,input().split())
balls=[[1,False] for _ in range(N+1)] #個数と赤がある可能性
balls[1]=[1,True]
for i in range(M):
    x,y=map(int,input().split())
    balls[x][0]-=1
    balls[y][0]+=1
    if balls[x][1]==True:
        balls[y][1]=True
    if balls[x][0]<=0:
        balls[x][1]=False
    

ans=0
for i in range(N+1):
    if     balls[i][1]==True:
        ans+=1
    
print(ans)


