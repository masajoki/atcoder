N=int(input())
T=list(map(int,input().split()))
sumT=sum(T)
target=max(sumT//2,sumT-sumT//2)


dp=[[0 for _ in range(target+10)] for _ in range(N+1)]


for i in range(N):
    for j in range(target+10):
        if j-T[i]>=0:
            if dp[i][j-T[i]]+T[i] <= target:
                dp[i+1][j]=max(dp[i][j],dp[i][j-T[i]]+T[i])
            else:
                dp[i+1][j]=dp[i][j]
        else:
                dp[i+1][j]=dp[i][j]

print(max(dp[N][target],sumT-dp[N][target]))

