import copy
N=int(input())
W=[]
for i in range(N):
    W.append(int(input()))

M=int(input())
A=[]
C=[]
CA=[]

for i  in range(M):
    a,c=map(int,input().split())
    A.append(a)
    C.append(c)
    CA.append((c/a,c,a))

W.sort(reverse=True)
CA.sort()

a=CA[0][2]
dp=[[-2 for _ in range(a+1)] for _ in range(N+1)]
dp[0][0]=-1
for i in range(N):
    dp[i][0]=-1
    for j in range(N+1):
        if j-W[i]>=0:
            if dp[i][j-W[i]]!=-2:
                dp[i+1][j]=j-W[i]    
            else:
                dp[i+1][j]=dp[i][j]
pass