N=int(input())
withdraw=[]
for i in range(1,10):
    if 6**i <=N:
        withdraw.append(6**i)
    if 9**i <=N:
        withdraw.append(9**i)

withdraw.sort()
withdraw.reverse()
dp=[[100001 for _ in range(N+10)] for _ in range(len(withdraw)+1)]
for i in range(N+1):
    dp[0][i]=i

dp[0][0]=0
for i in range(len(withdraw)):
    for j in range(N+2):
        if j-withdraw[i]>=0:
            for k in [1,2]:
                if j-withdraw[i]*k>=0:
                    dp[i+1][j]=min(dp[i][j-withdraw[i]*k]+k,dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]


print(dp[len(withdraw)-1][N])               
# print(dp[len(withdraw)-1])               

