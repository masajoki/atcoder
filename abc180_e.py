#bitdp 練習
N=int(input())
XYZ=[]
for i in range(N):
    xyz=tuple(map(int,input().split()))
    XYZ.append(xyz)

cost={}
for i in range(N):
    for j in range(N):
        a,b,c=XYZ[i]
        p,q,r=XYZ[j]
        cost[(i,j)]=abs(p-a)+abs(q-b)+max(0,r-c)

dp=[[10**18 for _ in range(N)] for _ in range(1<<N)] #2**N と同じ
dp[1][0]=0
for bit in range(2**N): #組み合わせを全部調べる
    for i in range(N): #全桁調べる
        if bit >> i & 1: #i桁目に1が立っていたら
            for j in range(N): #前桁調べる
                if bit >> j & 1 ==0 : #bitのj桁目が0
                    new = bit | 1<<j #newはbitのj桁目を1にしたもの
                    dp[new][j] = min(dp[new][j],dp[bit][i]+cost[(i,j)])

ans=10**18
for i in range(N):
    ans=min(ans,dp[-1][i]+cost[(i,0)])
print(ans)
