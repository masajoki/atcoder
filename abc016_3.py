N,M=map(int,input().split())
# A,B=[],[]
AB=[[] for _ in range(N+1)]
for i in range(M):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)
friendsfirnds=[set() for _ in range(N+1)]

for i in range(1,N+1):
    for f in AB[i]:
        for ff in AB[f]:
            if ff not in AB[i] and ff != i:
                friendsfirnds[i].add(ff)

for i in range(1,N+1):
    print(len(friendsfirnds[i]))
