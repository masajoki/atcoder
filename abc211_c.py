S=input()
N = len(S)

dp = [[0 for _ in range(N+1)] for _ in range(9)]
pattern = 'chokudai'
MOD = 10 ** 9 + 7
if S[0]=="c":
    dp[0][0]=1

for i in range(1,N):
    for j in range(8):
        if S[i]==pattern[j]:
            if j==0:
                dp[j][i]=dp[j][i-1]+1
            else:
                dp[j][i]=dp[j][i-1]+dp[j-1][i-1]
        else:
            dp[j][i]=dp[j][i-1]

print(dp[j][i]%MOD)
