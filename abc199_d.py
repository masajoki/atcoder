import sys
sys.setrecursionlimit(10**7)
N,M=map(int,input().split())
import copy
AB=[ [] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)

for ab in AB:
    if len(ab)>=3:
        print(0)
        exit()

points=0

chokusen=[]
loop=[]
pathes=0
ans=[]
visited=[False for _ in range(N+1)]
def dfs(current,path):
    global pathes , chokusen, pathes, loop
    visited[current]=True
    if len(AB[current])==1:
        #直線の端っこ
        chokusen.append(len(path)+1) 
        return

    for ab in AB[current]:
        if visited[ab]==False :
            p=copy.deepcopy(path)
            p.append(ab)
            return dfs(ab,p)
        elif visited[ab]==True: 
            if ab==path[0]:
                loop.append(len(path)+1)
            return

ans=1

for n in range(1,N+1):
    path=[n]
    if visited[n]==False:
        if len(AB[n])==0:
            visited[n]=True
            points+=1
        else:
            dfs(n,path)

ans*=3**points
loop.sort()
for i in range(len(loop)):
    if i %2==1:
        ans*=3*2**(loop[i]-2)

chokusen.sort()
for i in range(len(chokusen)):
    if i %2==1:
        ans*=3*2**(chokusen[i]-1)

print(ans)
