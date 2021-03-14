<<<<<<< HEAD
primes = [2]
A = int(input())
for L in range(3, A, 2): # 2 以外の素数は奇数なので
    if all(L % L2 != 0 for L2 in primes):  # すべての既存素数で割り切れなかったら素数
        primes.append(L)
print(primes)
=======
#N以下の素数列挙
import math
N=int(input())
A=[True for _ in range(N+1)]
for i in range(2,math.floor(math.sqrt(N))+1):
    if A[i]==True:
        for j in range(2,N//i+1):
            if i*j<=N:
                A[i*j]=False
            else:
                break

for i in range(2,N+1):
    if A[i]==True:
        print(i)
>>>>>>> 5bfaad7100611076a85ca73d213df447e697c805
