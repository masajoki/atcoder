import math
A,B=map(int,input().split())
GCD=math.gcd(A,B)

# 試し割りで因数分解する関数、aは本来リストだがsetに変更している。
def prime_factorize(n):
    a = set()
    while n % 2 == 0:
        a.add(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.add(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.add(n)
    return a

print(len(prime_factorize(GCD))+1)