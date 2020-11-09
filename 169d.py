import math
N=int(input())
if (N==0):
    print (0)

ans=1
max=int(math.sqrt(N)+1)

for n in range(2,max+1):
    if N%n == 0:
        ans+=1
        while N%n==0:
            N/=n
print(ans)
