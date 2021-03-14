N=int(input())
P=list(map(int,input().split()))
dp=[0 for _ in range(sum(P)+1)]
dp[0]=True
for p in P:
    dptemp=dp.copy()
    for i in range(sum(P)+1):
        if i-p>=0:
            if dptemp[i-p]==True:
                dp[i]=True
print(dp.count(True))
