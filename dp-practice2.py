# n個の品物がある
# i番目の品物の重さはweight[i]とvalue[i]
# weight, valueは整数
# 1<=weight, value<=1000
# 1<=W<=10000 (重さの総和がWを超えないようにする

#dp[i+1]:= i番目までの品物の中から、Wを超えないように選んだときの価値の総和の最大値
#とするとi-1番目のときの重さがわからないから、i番目が選べない。


#dp[i+1][weight]:= i番目までの品物の中から、wを超えないように選んだときの価値の総和の最大値
# とする

#dp[i][weight]が求まっている前提で、dp[i+1][weight]を求める

#品物 weight[i]value[i]を選ぶ場合dp[i+1][weight]は次のようになる

# dp[i+1][weight]=dp[i][weight-weight[i]]+value[i]
#
# weight-weight[i]は何をしている？その重さ前提でi-1まで選んだ最大のValueを取得している。
#
# 選ばない場合は次のようになる
# dp[i+1][weight]=dp[i][weight]

# 

N,W=map(int,input().split())
weight=[]
value=[]
for _ in range(N):
    vt,wt=map(int,input().split())
    weight.append(wt)
    value.append(vt)

dp=[[0 for _ in range(W+10) ] for _ in range(N+10)]

for i in range(N): #n-1番までループ
    for w in range(W+1): #weightはWまでループ
        if (w - weight[i])>=0:
            dp[i+1][w]=max(dp[i][w],dp[i][w-weight[i]]+value[i])
        else:
            dp[i+1][w]=dp[i][w]

print(dp[N][W])

