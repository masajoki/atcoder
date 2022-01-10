# Q2-5. 和が K 以上のペア
# アルゴ式
# 二分探索
import bisect
N,K=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
ans=0
for i in range(N):
    at=A[i]
    if at>=K:
        ans+=N
    else:
        t=K-at
        index=bisect.bisect_left(A,t)
        ans+=(N-index)
print(ans)
