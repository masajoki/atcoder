N=int(input())
A=[]
B=[]
C=[]
# それぞれi日にA、B,Cをやったときの幸せの最大値を入れる
dp=[[0,0,0] for _  in range(N+1)] 
for i in range(N):
    a,b,c=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

for i in range(N):
    dp[i+1][0]=max(dp[i][1]+A[i],dp[i][2]+A[i])
    dp[i+1][1]=max(dp[i][0]+B[i],dp[i][2]+B[i])
    dp[i+1][2]=max(dp[i][0]+C[i],dp[i][1]+C[i])

print(max(dp[N][0],dp[N][1],dp[N][2]))