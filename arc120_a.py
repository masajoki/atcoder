import heapq
import copy
N=int(input())
A=list(map(int,input().split()))

Amax=[ -1 for _ in range(N)]
Asum = [ 0 for _ in range(N)]
AsumSum = [ 0 for _ in range(N)]

Asum[0]=A[0]
AsumSum[0]=A[0]

tempMax=-1
for i in range(N):
    if A[i]>tempMax:
        tempMax=A[i]
    Amax[i]=tempMax
    if i>0:
        Asum[i]=Asum[i-1]+A[i]
        AsumSum[i]=AsumSum[i-1]+Asum[i]

for i in range(N):
    ans=(i+1)*Amax[i]
    ans+=AsumSum[i]
    print(ans)


