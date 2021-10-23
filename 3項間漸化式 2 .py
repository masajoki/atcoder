Q=int(input())

K=[]
for _ in range(Q):
    K.append(int(input()))
dp=[0 for _ in range(Q)]
dp[0]=1
dp[1]=1
for i in range(Q-2):
    dp[i+2]=dp[i+1]+dp[i]

for k in K:
    print(dp[k-1])
