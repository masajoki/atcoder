import bisect
N,Q=map(int,input().split())
A=list(map(int,input().split()))
A.sort()
T=[]
for i in range(Q):
    q=int(input())
    T.append(q)
    

for q in T:
    t=bisect.bisect_left(A,q)
    if t==N:
        print(0)
    else:
        print(N-t)


