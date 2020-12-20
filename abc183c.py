import itertools
N,K=map(int,input().split())
T=[[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    T[i]=list(map(int,input().split()))


if N==2:
    if T[0][1]+T[1][0] == K:
        print(1)
    else:
        print(0)
    exit()

templist=[]
permutlist=[]
for i in range(1,N):   
    templist.append(i)
    permutlist= list(itertools.permutations(templist))

ans=0
for l in permutlist:
    time=T[0][l[0]]
    for i in range(1,N-1):
        time+=T[l[i-1]][l[i]]
    time+=T[l[i]][0]
    if time==K:
        ans+=1

print(ans)