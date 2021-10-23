import itertools
N=int(input())
A=[]
for i in range(N):
    a=list(map(int,input().split()))
    A.append(a)

M=int(input())
XY=[[] for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    XY[x].append(y)
    XY[y].append(x)

combi=itertools.permutations(range(N),N)
ans=float("inf")
for C in combi:
    temp=0
    for i in range(N):
        if i!=0  :
            if  (C[i]+1) in XY[C[i-1]+1]:
                temp=float("inf")
                break
            else:
                temp+=A[C[i]][i]
        else:
            temp+=A[C[i]][i]
    ans=min(temp,ans)



if ans==float("inf"):
    print(-1)
else:
    print(ans)
    
    