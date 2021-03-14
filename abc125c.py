#回答みて1日寝かせて回答
#gcdのｇｃｄはｇｃｄなので、両側からｇｃｄしておいて真ん中をぬいてｇｃｄする（わかる？）

import math
N=int(input())
A=list(map(int,input().split()))
Agcd=[0 for _ in range(N)]
Agcd[0]=A[0]
AgcdRev=[0 for _ in range(N)]
AgcdRev[-1]=A[-1]
for n in range(1,N):
    gcd=math.gcd(Agcd[n-1],A[n])
    Agcd[n]=gcd

for n in range(N-1,0,-1):
    gcd=math.gcd(AgcdRev[n],A[n-1])
    AgcdRev[n-1]=gcd

maxGCD=0
for n in range(N):
    gcdn=n-1
    gcdrevn=n+1
    gcd=0
    gcdR=0
    if 0<=gcdn<N:
        gcd=Agcd[gcdn]
    if 0<=gcdrevn<N:
        gcdR=AgcdRev[gcdrevn]
    maxGCD=max(maxGCD,math.gcd(gcd,gcdR))
print(maxGCD)
