import math
a,b,c,d=map(int,input().split())
if d*c-b>a:
    print(1)
elif d*c-b<=0:
    print(-1)
else:
    print(math.ceil(a/(d*c-b)))
    