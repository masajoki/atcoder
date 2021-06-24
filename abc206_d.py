from collections import deque
N=int(input())
A=list(map(int,input().split()))
PATH=[set() for _ in range(10**5*2+10)]
visited=[ 0 for _ in range(10**5*2+10)]

for i in range(N//2):
    a=A[i]
    b=A[N-1-i]
    if a==b:
        continue
    else:
        PATH[a].add(b)
        PATH[b].add(a)


ans=0

q=deque()

for i in range(1,len(visited)):
    if len(PATH[i])==0:
        continue
    elif visited[i]==1:
        continue
    else:
        visited[i]=1
        for p in PATH[i]:
            if visited[p]==0:
                q.append(p)
        while len(q)>0:
            j=q.popleft()
            if visited[j]==0:
                ans+=1
                visited[j]=1
            else:
                continue

            for p in PATH[j]:
                if visited[p]==0:
                    q.append(p)

print(ans)


