import copy
N,M=map(int,input().split())

S=[]
for i in range(N):
    s=list(input())
    S.append(s)

def dfs(x,y,T):
    T[x][y]='#'
    temp=0
    for t in T:
        temp+=t.count('.')
    if temp==0:
        return True
    for a,b in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
        if 0<=a<N and 0<=b<M:
            if T[a][b]=='.':
                if dfs(a,b,T):
                    return True

ans=0
for i in range(N):
    for j in range(M):
        if S[i][j]=='#':
            T=copy.deepcopy(S)
            if dfs(i,j,T):
                ans+=1

print(ans)


