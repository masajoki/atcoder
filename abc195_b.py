import math
from decimal import Decimal
A,B,W=input().split()
a=Decimal(A)
b=Decimal(B)
w=Decimal(W)
w*=1000
ans1=0
ans2=0
temp=math.floor(w/a)
ta=w/temp
if ta<=b:
    ans1=temp

temp2=math.ceil(w/b)
tb=w/temp2
if tb>=a:
    ans2=temp2

if ans1==0 and ans2==0:
    print("UNSATISFIABLE")
    exit()
elif ans1==0 or ans2==0:
    ans1=max(ans1,ans2)
    ans2=ans1

print(ans2,ans1)
