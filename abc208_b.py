import math
P=int(input())
ans=0
for i in range(10,0,-1):
    c=math.factorial(i)
    temp=P//c
    ans+=temp
    P-=temp*c

print(ans)


