# 部分和問題：
# n 個の正の整数 a[0],a[1],…,a[n−1]a[0],a[1],…,a[n−1] と
# 正の整数 A が与えられる。
# これらの整数から何個かの整数を選んで総和が 
# A になるようにすることが可能か判定せよ。
# 可能ならば "YES" と出力し、不可能ならば "NO" と出力せよ。

# 【制約】
# ・1≤n≤100
# ・1≤a[i]≤1000
# ・1≤A≤10000

#ナップサック問題と同じで、価値の代わりに可能かどうかをboolで持つ

n,A=map(int,input().split())
a=list(map(int,input().split()))

# 
# 整数 a[i]を選ぶ場合、 (j >= a[i]の場合のみ)
#  dp [i][j-a[i]] を選んだ時総和をj とできるのなら、d[i+1][j]も

dp=[[False for _ in range(A+1) ] for _ in range(n+1)]
dp[0][0]=True

for i in range(n):
    for j in range(A+1):
        if j >= a[i]:
            dp[i+1][j]= (dp[i][j-a[i]] or dp[i][j])
        else:
            dp[i+1][j]=dp[i][j]

if dp[n-1][A]==True:
    print("YES")
else:
    print("NO")

