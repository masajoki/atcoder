from collections import deque
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

if S[Dh-1][Dw-1]=='#' or S[Ch-1][Cw-1]=='#':
    print(-1)
    exit() 

walkq=deque()
walkq.append((Ch,Cw))
while len(walkq)>0 :
    while len(walkq)>0:
        h,w=walkq.popleft()
        for i in range(h-2,h+3):
            for j in range(w-2,w+3):
                if 0<i<=H and 0<j<=W and S[i-1][j-1]=='.' :
                    if (i,j) not in ((h+1,w),(h-1,w),(h,w+1),(h,w-1),(h,w)):
                        if  dp[i][j]>(dp[h][w]+1):
                            dp[i][j]=dp[h][w]+1
                            walkq.append((i,j))
                    else:
                        if  dp[i][j]>(dp[h][w]):
                            dp[i][j]=dp[h][w]
                            walkq.appendleft((i,j))
                    
if dp[Dh][Dw]==inf:
    print(-1)
else:
    print(dp[Dh][Dw])
