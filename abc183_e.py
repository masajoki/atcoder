#解説AC
# DPした結果を累積和していく

H,W=map(int,input().split())
S=[]
for i in range(H):
    S.append(input())

mod=10**9+7

dp=[[0 for _ in range(W)] for _ in range(H)]

dpV=[[0 for _ in range(W)] for _ in range(H)] 
dpH=[[0 for _ in range(W)] for _ in range(H)]
dpD=[[0 for _ in range(W)] for _ in range(H)]

dp[0][0]=1
dpH[0][0]=0
dpV[0][0]=0
dpD[0][0]=0
for h in range(H):
    for w in range(W):
        if S[h][w]=='#':
            continue
        if h-1>=0 and S[h-1][w]=='.':  
            dp[h][w]+=dpV[h-1][w] %mod
        if w-1>=0 and S[h][w-1]=='.':  
            dp[h][w]+=dpH[h][w-1] %mod
        if h-1>=0 and w-1>=0  and S[h-1][w-1]=='.':
            dp[h][w]+=dpD[h-1][w-1] %mod


        if h-1>=0 and S[h-1][w]=='.':  
            dpV[h][w]+=dpV[h-1][w]  %mod
        if w-1>=0 and S[h][w-1]=='.':  
            dpH[h][w]+=dpH[h][w-1] %mod
        if h-1>=0 and w-1>=0  and S[h-1][w-1]=='.':
            dpD[h][w]+=dpD[h-1][w-1] %mod
        dpV[h][w]+=+dp[h][w]   %mod          
        dpH[h][w]+=+dp[h][w]   %mod          
        dpD[h][w]+=+dp[h][w]    %mod         

print(dp[h][w] %mod)
