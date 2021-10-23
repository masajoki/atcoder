H,W=map(int,input().split())
S=[]
for _ in range(H):
    s=input()
    S.append(s)

visited=[[0 for _ in range(W)]for _ in range(H)]

for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            for k in range(H):
                visited[k][j]=1
            for k in range(W):
                visited[i][k]=1
                    

ans=0
for i in range(H):
    ans+=sum(visited[i])

print(ans)