import copy
import sys
sys.setrecursionlimit(10**9) 
H,W=map(int,input().split())
r,c=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

ans=[["" for _ in range(W)] for _ in range(H)]

def dfs(h,w,invisited):
    invisited[h][w]=True

    a=ans[h][w]
    if a=="o":
        return True
    elif a=="x":
        return False

    if h==r and w==c:
        ans[h][w]="o"
        return True
    visited=copy.deepcopy(invisited)

    if S[h][w]=='v':
        if h+1<H  and visited[h+1][w]==False:
            if dfs(h+1,w,visited):
                ans[h+1][w]='o'
                return True
    elif S[h][w]=='^':
        if 0<=h-1  and visited[h-1][w]==False:
            if dfs(h-1,w,visited):
                ans[h-1][w]='o'
                return True
    elif S[h][w]=='>':
        if w+1<W  and visited[h][w+1]==False:
            if dfs(h,w+1,visited):
                ans[h][w+1]='o'
                return True
    elif S[h][w]=='<':
        if 0<=w-1  and visited[h][w-1]==False:
            if dfs(h,w-1,visited):
                ans[h][w-1]='o'
                return True
    elif S[h][w]=='.':
        if h+1<H and visited[h+1][w]==False:
            visited=copy.deepcopy(invisited)
            if dfs(h+1,w,visited):
                ans[h+1][w]='o'
                return True
        if 0<=h-1 and visited[h-1][w]==False:
            visited=copy.deepcopy(invisited)
            if dfs(h-1,w,visited):
                ans[h-1][w]='o'
                return True
        if w+1<W and visited[h][w+1]==False:
            visited=copy.deepcopy(invisited)
            if dfs(h,w+1,visited):
                ans[h][w+1]='o'
                return True
        if 0<=w-1 and visited[h][w-1]==False:
            visited=copy.deepcopy(invisited)
            if dfs(h,w-1,visited):
                ans[h][w-1]='o'
                return True

    
for i in range(H):
    for j in range(W):
        if S[i][j]=='#':
            ans[i][j]="#"
        else:
            visited=[[False for _ in range(W)] for _ in range(H)]
            if visited[i][j]==False and ans[i][j]=="":
                if dfs(i,j,visited):
                    ans[i][j]="o"
                else:
                    ans[i][j]="x"

for a in ans:
    print ("".join(a))