import copy
N=int(input())
A=list(map(int,input().split()))
dp=[[0 for _ in range(N+1)] for _ in range(N+1)]
dp[0]=copy.deepcopy(A)
for i in range(N):
	for j in range(N):
		for k in (-1,0,1):
			if 0<=j+k<N:
				dp[i+1][j]+=dp[i][j+k]
		dp[i+1][j]%=100

print(dp[N-1][N-1])