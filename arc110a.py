import math
N=int(input())
agcd=2
for i in range(2,N+1):
    agcd=math.gcd(i,agcd)

temp=math.factorial(N)+1
print(agcd)
print(math.factorial(N)+1)

for i in range(2,N+1):
    print(temp,i,temp%i)

temp=(16*27*25*7*11*13*17*19*23*29)+1

for i in range(2,N+1):
    print(temp,i,temp%i)
