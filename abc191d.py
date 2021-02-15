import decimal
import math
X,Y,R=map(decimal.Decimal,input().split())

Xmin=math.floor(X-R)
Xmax=math.ceil(X+R)
ans=0
for i in range(Xmin,Xmax+1):
    if i>=X-R and i<=X+R:
        Ytemp=(R**2-(i-X)**2).sqrt()
        Ytop=math.floor(Y+Ytemp)
        Ybotom=math.ceil(Y-Ytemp)
        ans+=(Ytop-Ybotom+1)
print(ans)