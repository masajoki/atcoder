#普通にやるとTLEまつりになるので、DPで探す回数を減らす
H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

ans=9999999999
dp=[[float("inf") for _ in range(W+1)] for _ in range(H+1)]
def dfs(h,w,color,count):
    global ans
    if count>=ans:
        return
    # print(h,w,color,count)
    if h==H-1 and w==W-1:
        # print(h,w,color,count,"return")
        ans=min(count,ans)
        return
    for x,y in ((h+1,w),(h,w+1)):
        if x<H and y<W:
            if color=='.' and S[x][y]=='#':
                temp=count+1
                if temp >= dp[x][y]:
                    continue
                else:
                    dp[x][y]=temp
                    dfs(x,y,S[x][y],temp)
            else:
                temp=count
                if temp >= dp[x][y]:
                    continue
                else:
                    dp[x][y]=temp
                    dfs(x,y,S[x][y],temp)

if S[0][0]=='#':
    dp[0][0]=1
    dfs(0,0,'#',1)
else:
    dp[0][0]=0
    dfs(0,0,'.',0)

print(ans)