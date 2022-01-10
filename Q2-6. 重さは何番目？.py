#Q2-6. 重さは何番目？
import bisect
N=int(input())
W=list(map(int,input().split()))
Ws=sorted(W)
for w in W:
    a=bisect.bisect_left(Ws,w)
    print(a)