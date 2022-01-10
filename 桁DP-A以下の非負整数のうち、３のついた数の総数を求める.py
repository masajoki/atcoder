#桁DP-A以下の非負整数のうち、３のついた数の総数を求める.py
from itertools import product
from collections import defaultdict
a=input()
n=len(a)

dp=defaultdict(int)
dp[0,False,False]=1
for i,less,has3 in product(range(n),(False,True),(False,True)):
    max_d=9 if less else int(a[i])
    for d in range(max_d+1):
        less_ = less or d < max_d
        has3_ = has3 or d == 3

        dp[i+1,less_,has3_] +=dp[i,less,has3]

print(sum(dp[n,less,True] for less in (False,True)))
