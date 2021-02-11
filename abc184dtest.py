A,B,C=map(int,input().split())

ap=0
dp=[[[0 for _ in range(11)] for _ in range(11) ]for _ in range(11)]
dp[A][B][C]=1
for i in range(A,10):
    for j in range(B,10):
        for k in range(C,10):
            dp[i+1][j][k]+=dp[i][j][k]*(i/(i+j+k))
            dp[i][j+1][k]+=dp[i][j][k]*(j/(i+j+k))
            dp[i][j][k+1]+=dp[i][j][k]*(k/(i+j+k))
            
# print(dp)
ans=0
for i in range(A,11):
    for j in range(B,11):
        for k in range(C,11):
            if k==10 or j==10 or i==10:
                print(i,j,k,dp[i][j][k])
                ans+=dp[i][j][k]
                pass

print(ans)
