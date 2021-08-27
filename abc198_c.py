import decimal
import math

R,X,Y=map(int,input().split())

if R**2==(X**2+Y**2):
    print(1)
    exit()
elif R**2 > (X**2+Y**2):
    print(2)
    exit()

dis=decimal.Decimal((X**2+Y**2)**0.5)
temp=decimal.Decimal(dis/R)
ans=math.ceil(temp)
print(ans)
