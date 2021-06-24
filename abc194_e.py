N,M=map(int,input().split())
A=list(map(int,input().split()))
inf=float("inf")
AmaxM=[0 for _ in range(N+1)]
AminM=[inf for _ in range(N+1)]


tempMax=0
tempMin=inf
for i in range(M):
    if A[i]>tempMax:
        tempMax=A[i]
    if A[i]<tempMin:
        tempMin=A[i]

for i in range(N):
    if A[i]==AmaxM[i]:
        AmaxM[i+1]=max(AmaxM[i],A[i])
    else:
        Amax[i+1]=Amax[i]
    if A[i]==AminM[i-M+1]:
        AminM[i]=min(AminM[i-M],A[i])
    else:
        AminM[i+1]=AminM[i]




