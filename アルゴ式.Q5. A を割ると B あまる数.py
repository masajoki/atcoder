#アルゴ式.Q5. A を割ると B あまる数.py
A,B=map(int,input().split())
import sys
input=sys.stdin.readline
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

divs=make_divisors(A-B)
ans=0
for d in divs:
    if d>B:
        ans+=1
print(ans)

