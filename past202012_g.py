H,W=map(int,input().split())
import copy
S=[]
K=0
for i in range(H):
    s=input()
    S.append(s)
    K+=s.count('#')

def dfs(h,w,k,visited):
    # print("    ",h,w,k,visited)

    if k==K:
        print(k)
        print(h+1,w+1)
        return True

    for i,j in ((h+1,w),(h-1,w),(h,w+1),(h,w-1)): #上下左右
        if 0<=i<H and 0<=j<W and S[i][j]=='#' and visited[i][j]==False:
            visitedcpy=copy.deepcopy(visited) 
            visitedcpy[i][j]=True
            if dfs(i,j,k+1,visitedcpy):
                print(h+1,w+1)
                return True

for i in range(H):
    for j in range(W):
        # print("  ",i,j)

        visited=[[False for _ in range(W)] for _ in range(H)]
        if S[i][j]=='#':
            visited[i][j]=True
            if dfs(i,j,1,visited):
                # print(i,j)
                exit()
