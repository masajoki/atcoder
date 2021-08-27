N,M=map(int,input().split())
A=list(map(int,input().split()))
# A.sort()

check=[ -1 for _ in range(M+1)]

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

for a in A:
    divs=prime_factorize(a)
    for d in divs:
        if d <=M  and check[d]==1:
            continue
        elif d!=1:
            i=d
            t=1
            while i <= M:
                check[i]=1
                t+=1
                i=d*t
print(check.count(-1)-1)
for t in range(1,M+1):
    if check[t]==-1:
        print(t)




