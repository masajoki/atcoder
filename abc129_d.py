import copy
H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

dp=[[-1 for _ in range(W)] for _ in range(H)]

for h in range(H):
    for w in range(W):
        if S[h][w]=='.':
            if w>=0:
                dp[h][w]=max(1,dp[h][w-1]+1)
            else:
                dp[h][w]=1
    for w in range(W-1,-1,-1):
        if 0<=w+1<W:
            if dp[h][w]!=-1 and dp[h][w+1]!=-1:
                dp[h][w]=dp[h][w+1]
dpw=copy.deepcopy(dp)

dp=[[-1 for _ in range(W)] for _ in range(H)]

for w in range(W):
    for h in range(H):
        if S[h][w]=='.':
            if h>=0:
                dp[h][w]=max(1,dp[h-1][w]+1)
            else:
                dp[h][w]=1
    for h in range(H-1,-1,-1):
        if 0<=h+1<H:
            if dp[h][w]!=-1 and dp[h+1][w]!=-1:
                dp[h][w]=dp[h+1][w]

dph=copy.deepcopy(dp)

ans=0
for h in range(H):
    for w in range(W):
        temp=dph[h][w]+dpw[h][w]-1
        ans=max(ans,temp)
print(ans)
