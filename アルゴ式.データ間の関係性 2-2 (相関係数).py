#アルゴ式.データ間の関係性 2-2 (相関係数).py

import statistics
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
Amean=statistics.mean(A)
Bmean=statistics.mean(B)
Astdev=statistics.pstdev(A)
Bstdev=statistics.pstdev(B)
kyobunsan=0

for i in range(N):
    t1=Amean-A[i]
    t2=Bmean-B[i]
    kyobunsan+=t1*t2/N

r=kyobunsan/Astdev/Bstdev
print(r)