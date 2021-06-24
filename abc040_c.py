N=int(input())
A=list(map(int,input().split()))
dp=[0 for _ in range(100000+10)]

for i in range(1,N):
    cost1=99999
    cost2=99999
    if i-1>=0:
        cost1=dp[i]+abs(A[i]-A[i-1])
    if i-2>=0:
        cost2=dp[i-1]+abs(A[i]-A[i-2])
    dp[i+1]=min(cost1,cost2)

print(dp[N])