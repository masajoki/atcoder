N=int(input())
S=[input() for i in range(N)]
DP=[[0,0] for i in range(N+1)]
DP[0]=[1,1]
for i in range(N):
  for j in range(2):
    for k in range(2):
      if S[i]=='AND':
        DP[i+1][min(j,k)]+=DP[i][j]
      else:
        DP[i+1][max(j,k)]+=DP[i][j]
print(DP[N][1])
