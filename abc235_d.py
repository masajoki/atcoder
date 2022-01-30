#abc235_d.py
#黒板のxは最初1
from collections import deque
from collections import defaultdict
a,N=map(int,input().split())
x=1
queue=deque()
visited=defaultdict(int)
queue.append((1,0))
ans=10**10
while len(queue)>0:
    d,c=queue.popleft()
    if d==N:
        ans=min(c,ans)
    dstr=str(d)
    dlen=len(dstr)
    if d>=10 and d%10!=0:
        for i in range(len(dstr)-1):
            tempstr=dstr[-1]+dstr[:dlen-1]
            temp=int(tempstr)
            visitedcnt=visited[temp]
            if visitedcnt==0 or c+1 < visitedcnt:
                queue.append((temp,c+1))
                visited[temp]=c+1
    temp=d*a
    if len(str(temp))<=len(str(N)):
        visitedcnt=visited[temp]
        if visitedcnt==0 or c+1 < visitedcnt:
            queue.append((temp,c+1))
            visited[temp]=c+1

if ans==10**10:
    print(-1)     
else:
    print(ans)