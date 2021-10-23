import itertools
N,M=map(int,input().split())
ABI=[]

for i in range(N):
    a,b=map(int,input().split())
    ABI.append([a,b,i])

ans=10**9
F=itertools.permutations(range(N))

for f in F:

    totaltime=0
    last=0
    sabo=False
    unsatisfy=0
    for i in range(len(f)):
        fi=f[i]
        waitmealtime=last+ABI[fi][0]
        totaltime+=waitmealtime
        last=waitmealtime

        for t in range(i):
            fronti=ABI[f[t]][2]
            if fronti>fi:
                unsatisfy+=ABI[fi][1]

    # print(totaltime,unsatisfy)
    if unsatisfy>M:
        continue
    else:
        ans=min(ans,totaltime)

print(ans)
    

