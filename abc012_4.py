N,M=map(int,input().split())
AB=[[] for _ in range(N+1)]
T=[[float("inf") for _ in range(N+1)]for _ in range(N+1)]
for i in range(N+1):
    T[i][0]=0
    T[0][i]=0
    T[i][i]=0

for i in range(M):
    a,b,t=map(int,input().split())
    if a>b:
        a,b=b,a
    AB[a].append(b)
    AB[b].append(a)
    T[a][b]=t
    T[b][a]=t

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            T[i][j]=min(T[i][j],T[i][k]+T[k][j])

ans=float('inf')
for i in range(1,N+1):
    ans=min(max(T[i]),ans)

print(ans)
