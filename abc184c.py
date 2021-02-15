a,b=map(int,input().split())
x,y=map(int,input().split())

if a==x and b==y:
    print(0)
    exit()

chikaku=abs(a-x)+abs(b-y)
if chikaku <=3:
    print(1)
    exit()

if b!=y:
    naname=abs((a-x)/(b-y))
    if naname==1:
        print(1)
        exit()

uppper=0
lower=0
if a!=x:
    uppper=abs((b+3-y)/(a-x))
    lower=abs((b-3-y)/a-x)
else:
    uppper=abs((a+3-x)/(b-y))
    lower=abs((a-3-x)/(b-y))
 
if max(uppper,lower) >=1 and min(uppper,lower) <= 1:
    print(2)
else:
    print(3)








