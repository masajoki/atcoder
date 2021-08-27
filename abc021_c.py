from collections import deque
N=int(input())
a,b=map(int,input().split())
M=int(input())
XY=[[] for _ in range(N+1)]

for i in range(M):
    x,y=map(int,input().split())
    XY[x].append(y)
    XY[y].append(x)

visited=[ [float("inf"),0] for _ in range(N+1)] # steps to x, number of ways to x

mod=10**9+7
q=deque()
q.append((a,0)) # x, steps to x


#幅優先探索と動的計画法の組み合わせで解いた（動的計画法のつもりはなかったが結果的にそうなった）
visited[a]=[0,1]
while len(q)>0:
    x,stepToX=q.popleft()

    for y in XY[x]:
        stepsToY,waysToY=visited[y]
        if stepsToY > stepToX+1: #より短い経路である場合
            visited[y]=[stepToX+1,visited[x][1]] #Yまでの距離はXまでの距離＋１、Xまでの経路の数をYまでの経路の数とする
            q.append((y,stepToX+1))
        elif stepsToY==stepToX+1: #知られているYまでの経路の数と同じ場合
            visited[y]=[stepsToY,waysToY+visited[x][1]] #Yまでの距離はそのまま、Xまでの経路の数をYまでの経路の数に足す

print(visited[b][1]%mod)
