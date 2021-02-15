import itertools
N=int(input())
x=[]
y=[]
for i in range(N):
    xt,yt=map(int,input().split())
    x.append(xt)
    y.append(yt)

routes=list(itertools.permutations(range(N),N))


pathlength=0
for i in range(len(routes)):
    for j in range(N-1):
        pathlength+=((x[routes[i][j+1]]-x[routes[i][j]])**2 +  (y[routes[i][j+1]]-y[routes[i][j]])**2 )**0.5

print(pathlength/len(routes))



