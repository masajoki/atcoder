import math
N=int(input())
X=list(map(int,input().split()))
primes=(2,3,5,7,11,13,17,19,23,29,31,37,41,43,47)
candidate=[]
for i in range(2**len(primes)):
    temp=1
    for j in range(len(primes)):
        if i >> j &1:
            temp*=primes[j]
    candidate.append(temp)

candidate.sort()

for c in candidate:
    ok=True
    for x in X:
        if math.gcd(x,c)==1:
            ok=False
            break
    if ok:
        print(c)
        exit()
