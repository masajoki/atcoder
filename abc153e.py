H,N=map(int,input().split())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

dp=[[9999999999 for _ in range(H+1)] for _ in range(N+1)]

k=1
for j in range(H+1):
    if j>A[0]*k:
        k+=1
    dp[0][j]=B[0]*k


for i in range(N):
    for j in range(H+1):
        k=1
        # if j-A[i]>=0:
        T=dp[i][j]
        while True:
            p=max(0,j-A[i]*k)
            temp=dp[i][p]+B[i]*k
            T=min(T,temp)
            k+=1
            if j-A[i]*k < 0:
                break
        dp[i+1][j]=T
        # else:
        #     dp[i+1][j]=dp[i][j]
print(dp[N][H])

# print(dp)