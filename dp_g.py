N,M=map(int,input().split())
dp=[0 for _ in range(N+1)]
path=[[] for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    path[x].append(y)

def dosome(x,step):
    global path
    global dp
    if dp[x]> step:
        return
    else:
        dp[x]=step

    if len(path[x])!=0:
        ylist=path[x]
        step+=1
        for y in ylist:
            dosome(y,step)

for i in range(1,N+1):
    t=i
    step=0
    dosome(t,0)

# print(dp)
print(max(dp))