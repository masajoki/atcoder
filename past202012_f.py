N,M=map(int,input().split())

count=[ [set() for _ in range(N+1)]for _ in range(N+1)]
for i in range(M):
    a,b,c=map(int,input().split())
    count[a][b].add(c)
    count[b][c].add(a)
    count[a][c].add(b)

ans=0
for i in range(N+1):
    for j in range(N+1):
        ans=max(ans,len(count[i][j]))
print(ans)