import bisect
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort()
B.sort()

ans=float("inf")
for a in A:
    i=bisect.bisect_left(B,a)
    j=bisect.bisect_right(B,a)
    temp=float("inf")
    for t in (i-1,i,i+1,j-1,j,j+1):
        if 0<=t<M:
            ans=min(ans,abs(B[t]-a))
print(ans)
