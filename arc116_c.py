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



N,M=map(int,input().split())
mod=998244353
mdivs=prime_factorize(M)

mdivlen=len(mdivs)+1
count=[ [1 for _ in range(N)] for _ in range(mdivlen) ]
ans=0

for i in range(mdivlen):
    for j in range(N):
        if i-1>=0 and j-1>=0:
            count[i][j]=count[i-1][j]+count[i][j-1]
print(count[mdivlen-1][N-1]%mod)
            


