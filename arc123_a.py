import math
A=list(map(int,input().split()))
a,b,c=A
if 2*b==(a+c):
    print(0)
elif 2*b<(a+c):
    temp=math.ceil((a+c)/2)
    if temp==(a+c)//2:
        ans=temp-b
        print(ans)
    else:
        ans=temp-b+1
        print(ans)
elif 2*b>=(a+c):
    temp=2*b-a-c
    print(temp)

