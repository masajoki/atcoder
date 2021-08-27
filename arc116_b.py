N=int(input())
A=list(map(int,input().split()))
mod=998244352

ans=0
temp=0

for a in A:
    ans=(ans+a**2)%mod

for i in range(N):
    temp=(temp+A[i]*pow(2,mod))%mod

for i in range(N):
    temp=temp-A[i]%
    temp=temp//


