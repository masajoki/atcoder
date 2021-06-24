N,M=map(int,input().split())
S=[]
for i in range(N):
    S.append(input())

ans=[[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        for x in (i-1,i,i+1):
            for y in (j-1,j,j+1):
                if 0<=x<N and 0<=y<M :
                    if S[x][y]=='#' :
                        ans[i][j]+=1

for i in range(N):
    for j in range(M):
        print(ans[i][j],end="")
    print()
