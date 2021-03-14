x1,y1,R=map(int,input().split())
x2,y2,x3,y3=map(int,input().split())

tl=(x2-x1)**2+(y3-y1)**2
tr=(x3-x1)**2+(y3-y1)**2
bl=(x2-x1)**2+(y2-y1)**2
br=(x3-x1)**2+(y2-y1)**2
t=y1+R
b=y1-R
r=x1+R
l=x1-R

if t<=y3 and r<=x3 and l>=x2 and b>=y2:
    print("NO")
else:
    print("YES")

if max(tr,tl,bl,br)>R**2:
    print("YES")
else:
    print("NO")