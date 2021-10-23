N=int(input())
A=[]
dp=[[0 for _ in range(3)]for _ in range(N+1)]

for i in range(N):
    a=list(map(int,input().split()))
    A.append(a)

for i in range(N):
    maxsal=0
    for j in range(3):
        for k in range(3):
            if j!=k:
                dp[i+1][j]=max(dp[i+1][j],dp[i][k]+A[i][j])

print(max(dp[N]))
        
            