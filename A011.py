D,N=map(int,input().split())
A=[]
for _ in range(N):
    a=int(input())
    A.append(a)
for _ in range(N):
    dp=[[0 for _ in range(2*D+1)] for _ in range(N+1)]
    dp[0][D]=-1

for i in range(N):
    for j in range(D*2+1):
        a=A[i]
        if 0 <= j-a <= 2*D and dp[i][j-a]!=0: 
            dp[i+1][j]=j-a
        if 0 <= j+a <= 2*D and dp[i][j+a]!=0: 
            dp[i+1][j]=j+a

from collections import deque
Q=deque()
lastindex=0
for i in range(len(dp[N])):
    if dp[N][i]!=0:
        lastindex=i
for n in range(N,0,-1):
    last=dp[n][lastindex]
    # beforelast=dp[n-1][last]
    if lastindex<last:
        Q.appendleft("L")
    else:
        Q.appendleft("R")
    lastindex=last

while len(Q)>0:
    a=Q.popleft()
    print(a,end="")
print()
