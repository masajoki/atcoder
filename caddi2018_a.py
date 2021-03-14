import collections
n,p=map(int,input().split())
def prime_factorize(n): #因数分解
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

c=collections.Counter(prime_factorize(p))
ans=1
for i in c.items():
    if i[1]>=n:
        ans*=i[0]**(i[1]//n)

print(ans)
