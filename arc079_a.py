N,M=map(int,input().split())
# A,B=[],[]
AB=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)

for b in AB[N]:
    for a in AB[b]:
        if a==1:
            print("POSSIBLE")
            exit()
print("IMPOSSIBLE")
