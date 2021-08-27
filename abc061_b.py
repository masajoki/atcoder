N,M=map(int,input().split())
AB=[[] for _ in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)

for i in range(1,N+1):
    print(len(AB[i]))