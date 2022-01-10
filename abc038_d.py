N=int(input())
W=[]
H=[]
WH=[]
 
dp=[0 for _ in range(N+1)]
for i in range(N):
    w,h=map(int,input().split())
    W.append(w)
    H.append(h)
    WH.append((w,h))

WH.sort()
for i in range(N):
    temp=0
    for j in range(i):
        if WH[j][0]<WH[i][0] and WH[j][1]<WH[i][1]:
            temp=max(dp[i],dp[j]+1)
    dp[i]=max(dp[i],temp)

print(max(dp)+1)


