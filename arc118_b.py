import math
K,N,M=map(int,input().split())
A=list(map(int,input().split()))

B=[]
Bt=[]
Bmin=[]
NMgcd=math.gcd(N,M)
NMlcm=N*M//NMgcd

At=[]
for a in A:
    t=a*M//NMgcd
    At.append(t)

for a in A:
    t=a*M//N
    B.append(t)
    bt=t*N//NMgcd
    Bt.append(bt)

if sum(Bt)==M:
    for b in Bt:
        print(b, end=" ")
    exit()


diff=M-sum(B)

bMaxMin=10**9
bMaxMinIndex=-1
for i in range(K):
    t=B[i]+1
    bt=t*N//NMgcd
    b2=abs(At[i]-bt)
    Bmin.append((b2,i))

Bmin.sort()
for i in range(diff):
    j=Bmin[i][1]
    B[j]+=1

for b in B:
    print(b, end=" ")

print()

