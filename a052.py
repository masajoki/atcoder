N=int(input())
A,B=map(int,input().split())
visited=[0 for _ in range(N+1)]
visited[0]=1
visited[N]=1
for i in range(N+1):
    a=i-A
    b=i-B
    if 0<=a<=N:
        if visited[a]==1:
            visited[i]=1
    if 0<=b<=N:
        if visited[b]==1:
            visited[i]=1

print(visited.count(0))
