primes = [2]
A = int(input())
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    if all(L % L2 != 0 for L2 in primes):  # すべての既存素数で割り切れなかったら素数
        primes.append(L)
print(primes)