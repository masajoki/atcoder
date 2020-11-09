#C - Sum of gcd of Tuples (Easy)
# 1<=K<=200
# Kは整数
import math

K=int(input())

ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            gcg=math.gcd(math.gcd(a,b),c)
            ans+=gcg
print(ans)