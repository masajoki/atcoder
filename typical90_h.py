#耳DPというらしい。
#https://atcoder.jp/contests/typical90/tasks/typical90_h

#類題
# https://atcoder.jp/contests/yahoo-procon2019-qual/tasks/yahoo_procon2019_qual_d
N = int(input())
S = input()

dp = [[0 for _ in range(N+1)] for _ in range(8)]
pattern = 'atcoder'
MOD = 10 ** 9 + 7
if S[0]=="a":
    dp[0][0]=1

for i in range(1,N):
    for j in range(7):
        if S[i]==pattern[j]:
            if j==0:
                dp[j][i]=dp[j][i-1]+1
            else:
                dp[j][i]=dp[j][i-1]+dp[j-1][i-1]
        else:
            dp[j][i]=dp[j][i-1]

print(dp[j][i]%MOD)



# # dp[i][j]  部分列 S[:i] に部分列 match[:j] が含まれる通り数
# dp = [[0] * (len(match) + 1) for _ in range(N + 1)]

# for j in range(len(match) + 1):
#     for i in range(N + 1):
#         if j == 0:
#             dp[i][0] = 1
#         elif i == 0:
#             dp[0][j] = 0
#         elif S[i - 1] == match[j - 1]:
#             dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % MOD
#         else:
#             dp[i][j] = dp[i - 1][j]

# print(dp[N][len(match)])