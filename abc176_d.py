import sys
sys.setrecursionlimit(10**9)
H,W=map(int,input().split())
Ch,Cw=map(int,input().split())
Dh,Dw=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())
inf=float("inf")
dp=[[inf for _ in range(W+1) ]for _ in range(H+1)]
visited=[[False for _ in range(W+1) ]for _ in range(H+1)]
dp[Ch][Cw]=0

def dfs(h,w):
    visited[h][w]=True
    global dp
    if h==Dh and w==Dw:
        return
    warp=True
    for i,j in ((h+1,w),(h-1,w),(h,w+1),(h,w-1)):
        if 0<i<=H and 0<j<=W and S[i-1][j-1]=='.':
            if dp[i][j]>dp[h][w]:
                dp[i][j]=dp[h][w]
                warp=False
                dfs(i,j)
            else:
                break
    if warp:
        for i in range(h-2,h+3):
            for j in range(w-2,w+3):
                if 0<i<=H and 0<j<=W and S[i-1][j-1]=='.' :
                    if  dp[i][j]>dp[h][w]+1:
                        dp[i][j]=dp[h][w]+1
                        dfs(i,j)

dfs(Ch,Cw)
if dp[Dh][Dw]==inf:
    print(-1)
else:
    print(dp[Dh][Dw])
