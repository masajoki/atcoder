A,B,C=map(int,input().split())

ap=0
dp=[[[0 for _ in range(101)] for _ in range(101) ]for _ in range(101)]

for i in range(A,100):
    for j in range(B,100):
        for k in range(C,100):
            # dp[i+1][j][k]=dp[i][j][k]+(i/(i+j+k))
            # dp[i][j+1][k]=dp[i][j][k]+(j/(i+j+k))
            # dp[i][j][k+1]=dp[i][j][k]+(k/(i+j+k))
            dp[i+1][j][k]=(i/(i+j+k))
            dp[i][j+1][k]=(j/(i+j+k))
            dp[i][j][k+1]=(k/(i+j+k))

# print(dp)
ans=0
for i in range(A,101):
    for j in range(B,101):
        for k in range(C,101):
            if k==100 or j==100 or i==100:
                ans+=dp[i][j][k]

print(ans)
