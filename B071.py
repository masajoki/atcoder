N,M=map(int,input().split())
W=[]
Wcount={}
for i in range(N):
    w=int(input())
    W.append(w)
for i in range(N):
    w=W[i]
    if w in Wcount.keys():
        Wcount[w]+=1
    else:
        Wcount[w]=1

parweight=[]

for i in Wcount.items():
    w=i[0]
    c=i[1]//2
    for j in range(c):
        parweight.append(w*2)

# if sum(parweight)<=M:
#     print(sum(parweight))
#     exit()


dp=[[0 for _ in range(M+1)] for _ in range(len(parweight)+1)]
dp[0][0]=1
for i in range(len(parweight)):
    for j in range(M+1):
        p=parweight[i]
        if j-p>=0 and dp[i][j-p]==1:
            dp[i+1][j]=max(dp[i+1][j-p],dp[i][j])
        else:
            dp[i+1][j]=max(dp[i+1][j],dp[i][j])

ans=0
for i in range(M+1):
    t=dp[len(parweight)][i]
    if t==1:
        ans=i

print(ans)
