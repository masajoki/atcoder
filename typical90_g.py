import bisect
N=int(input())

A=list(map(int,input().split()))
A.sort()
B=[]
Q=int(input())

for i in range(Q):
    b=int(input())
    B.append(b)


for b in B:
    i=bisect.bisect_left(A,b)
    j=bisect.bisect_right(A,b)
    temp=10**10
    for t in (i-1,i,i+1,j-1,j,j+1):
        if 0<=t<N:
            temp=min(temp,abs(A[t]-b))
    
    print(temp)
