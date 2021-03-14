# n個の整数から何個か整数を選んだ時の総和の最大値は？

# dp[0]:= 何も選ばない
# dp[1]:= 0番目まで（a[0]まで）数字を選んだときの総和の最大値
# dp[2]:= 1番目まで（a[1]まで）数字を選んだときの総和の最大値
# dp[i+1]:= i番目まで(a[i]まで)　数字を選んだときの総和の最大値

# 求める値は dp[n]

# ・1≤n≤10000
# ・−1000≤a[i]≤1000

n=int(input())
a=list(map(int,input().split()))

dp=[ 0 for _ in range(n+1)]

for i in range(n):
    dp[i+1]=max(dp[i],dp[i]+a[i])

print(dp[n])