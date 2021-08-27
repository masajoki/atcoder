#T90-042
k=int(input())
#各桁の数の合計が9で割り切れれば9の倍数である
#この手の問題は動的計画法でやると良い
mod=10**9+7
ans=0
dp=[0 for _ in range(k+1)]
dp[0]=1 #DP[0]=1にしておかないと、最初の数字が表現できない。

if k%9!=0:
    print(0)
    exit()
for i in range(1,k+1):
    for j in range(1,10):
        if i-j>=0:
            dp[i]+=dp[i-j]
            dp[i]%=mod
ans=dp[k]%mod
print(ans)

