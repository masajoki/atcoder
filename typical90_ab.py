#2次元いもす法
N=int(input())

xmax=0
ymax=0

D=[[0 for _ in range(1002) ] for _ in range(1002)]

for i in range(N):
    # 原点左下、左下x,y、右上x2,y2
    x,y,x2,y2=map(int,input().split())
    xmax=max(x,x2,xmax)
    ymax=max(y,y2,ymax)
    D[y][x]+=1 #左上
    D[y2][x]-=1 #右上 
    D[y][x2]-=1 #左下
    D[y2][x2]+=1 #右下


for y in range(ymax+1):
    for x in range(xmax+1):
        D[y][x]+=D[y][x-1]
for x in range(xmax+1):
    for y in range(ymax+1):
        D[y][x]+=D[y-1][x]

Ans=[0 for _ in range(N+1)]
for y in range(ymax+1):
    for x in range(xmax+1):
        Ans[D[y][x]]+=1

for i in range(1,N+1):
    print(Ans[i])
