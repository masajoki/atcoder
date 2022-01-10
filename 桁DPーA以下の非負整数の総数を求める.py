# 桁DPーA以下の非負整数の総数を求める

from itertools import product
from collections import defaultdict

a=input()
n=len(a)

dp=defaultdict(int)
dp[0,False]=1

#less: 直前の桁の数字はaの桁iより小さい場合
for i ,less in product(range(n),(True,False)):

    max_d=9 if less else int(a[i]) #lessがTrueだったら max_d=9, じゃなかったら1 max_d=int(a[i])

    for d in range(max_d+1): #0~９までか、または a[i]まで
        less_ = less or d < max_d # less_ は less がすでに Trueか、または d が max_dより小さいとTrue
        dp[ i+1,less_ ] += dp[i,less]

print(sum(dp[n,less] for less in (0,1)))


