N=int(input())
A=list(map(int,input().split()))

T=[0 for _ in range(10**5+1)]
for i in range(N):
    T[A[i]]=i

ans=0
for i in range(10**5+1):
    if T[i]==0:
        continue
    ans=A[T[i]]
    for i in range(1,N):
        if A[T]
