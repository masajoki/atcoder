N=int(input())
A=list(map(int,input().split()))
a=0
b=0
c=0
import math
for i in range(N):
    a+=i
    b+=2*(i-A[i])
    c+=A[i]**2+i**2-2*i*A[i]
x=math.ceil((-1*b+math.sqrt(b**2-4*a*c))/(2*a))

ans=0
for i in range(N):
    ans+=abs(i-(x+1))

print(ans)