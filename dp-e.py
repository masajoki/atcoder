#Wが10**9まで取りうるので、配列はアイテムと価値の二次元にして、
# 通常なら価値を入れる配列の値に重量を入れていく。
# なお価値の範囲は 0 〜全部選択したとき。
# v 10**3, 100こまでなので 100* 10**3までしかいかない
N,W=map(int,input().split())
w=[]
v=[]

vmax=0
for _ in range(N):
    wt,vt=map(int,input().split())
    w.append(wt)
    v.append(vt)
    vmax+=vt

dp=[[ 999999999 for _ in range(vmax+1)  ] for _ in range(N+1)]
# for i in range(N+1):
#     dp[i][0]=0

dp[0][0]=0
for i in range(N):
    for vl in range(vmax+1):
        if (vl - v[i] >= 0) :
            dp[i+1][vl] = min (dp[i][vl], dp[i][vl-v[i]]+ w[i])

        else:
            dp[i+1][vl] = min(dp[i][vl],dp[i+1][vl])
ans=0
for i in range(vmax+1):
    if dp[N][i]<=W:
        ans=i
print(ans)