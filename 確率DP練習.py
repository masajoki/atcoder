# 1 から 6 までの整数が等確率に出るサイコロが 1 つある．このサイコロを
# N 回振るとき，出た目の数の和が K 以上になる確率を求めよ．
# 1 ≤ N ≤ 2 × 10**3
# 1 ≤ K ≤ 6 × N

# サンプル
# 入力 1: 1 4 出力 1: 0.500000000000
# 入力 2: 3 5 出力 2: 0.981481481481
N,K=map(int,input().split())
dp=[[0 for _ in range(N*6+10)] for _ in range(N+1)]

for i in range(K+1):
    dp[0][i]=1/6

for i in range(N):
    for j in range(i,K+10):
        for k in range(1,7):
            if j-k>=1:
                dp[i+1][j]+=dp[i][j-k]*(1/6)
pass

