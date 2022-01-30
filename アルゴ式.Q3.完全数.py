#アルゴ式.Q3.完全数.py
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

N=int(input())
divs=make_divisors(N)

t=0
for a in divs[:len(divs)-1]:
    t+=a
    if t>N:
        print("No")
        exit()

if t==N:
    print("Yes")
else:
    print("No")


