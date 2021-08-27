N,M=map(int,input().split())
C=[[float('inf') for _ in range(N+1)]for _ in range(N+1)]
for i in range(N+1):
    C[i][i]=0
D=[[] for _ in range(M+1)]

for i in range(M):
    a,b,c=map(int,input().split())
    D[i]=[a,b]
    C[a][b]=c

import copy
ans=0
for m in range(1,N+1):
    Cm=copy.deepcopy(C)
    
    for k in range(1,m+1):
        for i in range(1,N+1):
            for j in range(1,N+1):
                Cm[i][j]=min(Cm[i][j], Cm[i][k] + Cm[k][j])
    
    for i in range(N+1):
        for j in range(N+1):
            if Cm[i][j]!=float('inf'):  
                ans+=Cm[i][j]

print(ans)