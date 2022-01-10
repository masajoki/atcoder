# abc029_d
# 問題文
# 高橋君は 1 以上 N 以下のすべての整数を十進表記で一回ずつ紙に書きました。
# この作業で、高橋君は 1 という数字を何個書いたでしょうか。
# 桁DPの練習
# 以下の写経
# https://zehnpaard.hatenablog.com/entry/2018/06/24/215607

# 桁DPーA以下の非負整数の総数を求める

from itertools import product
from collections import defaultdict

a=input()
n=len(a)

dp=defaultdict(int)
dp[0,False,False]=[1,0]

#less: 直前の桁の数字はaの桁iより小さい場合
for i ,less,has1 in product(range(n),(True,False),(True,False)):

    max_d=9 if less else int(a[i]) #lessがTrueだったら max_d=9, じゃなかったら1 max_d=int(a[i])

    for d in range(max_d+1): #0~９までか、または a[i]まで
        less_ = less or d < max_d # less_ は less がすでに Trueか、または d が max_dより小さいとTrue
        has1_ = has1 or d == 1
        one = 1 if d ==1 else 0
        dp[ i+1,less_ ,has1_] += dp[i,less,has1] 

print(sum(dp[n,less,True] for less in (0,1)))

