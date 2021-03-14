#Nも(N+1)/2も素数 を満たす奇数Nの数を出力する

Q=int(input())
L=[]
R=[]
maxR=0

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]

for i in range(Q):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)
    maxR=max(maxR,r)

Primes=primes(maxR)
PrimesCount=[0 for _ in range(100001)]

for i in Primes:
    if int((i+1)/2) in Primes:
        PrimesCount[i]=1

pass
nowcount=0
for i in range(len(PrimesCount)):
    if PrimesCount[i]==1:
        nowcount+=1
    PrimesCount[i]=nowcount

    


for i in range(Q):
    print(PrimesCount[R[i]]-PrimesCount[L[i]-1])


