import math
n=int(input())
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())

bn=min(a,b,c,d,e)
tt=math.ceil(n/bn)
ans=tt+4
print(ans)