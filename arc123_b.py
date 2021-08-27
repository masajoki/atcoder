import bisect
N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()

ans=0
j=0
k=0

bl=0
cl=0

for i in range(N):
    if bl>=N or cl>=N:
        break
    j=bisect.bisect_right(B,A[i],lo=bl)
    if j==N:
        continue
    else:
        bl=j+1
        k=bisect.bisect_right(C,B[j],lo=cl)
        if k==N:
            continue
        else:
            cl=k+1
            ans+=1
print(ans)
