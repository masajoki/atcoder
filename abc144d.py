import math
a,b,x=map(int,input().split())
temp=0
if x>(a*a*b/2):
    temp=math.atan(2*(b/a - x/a**3))

else:
    temp=math.atan((b**2*a/(2*x)))
print(math.degrees(temp))
