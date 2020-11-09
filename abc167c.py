# アルゴリズムM個
# それぞれの理解度は0
# N冊の参考書
# i番目の参考書 (1<=i<=N)　はCi円で販売
# j (1<=j<=M)についてj番目のアルゴリズムの理解度が Aij上がる
# M個すべてのアルゴリズムの理解度をX以上にできるか、いくらかかるか

# N M X
# C1 A11, ... , A1m
# ...
# Cn An1, ..., Amm

import numpy as np
import itertools
n,m,x=map(int,input().split())

As=np.zeros((n,m+1))

for i in range(0,n):
    As[i]=map(int,input().split(' '))

for k in range(1,n+1):
    for p in itertools.permutations(As,k):
        s=sum(p)


