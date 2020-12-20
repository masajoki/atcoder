a,b,x,y=map(int,input().split())
time=100000000000
if a==b:
    time=x
elif a>b:
    time=x+min((abs(a-b)-1)*2*x,(abs(a-b)-1)*y)
elif a<b:
    time=x+min((abs(a-b))*2*x,(abs(a-b))*y)
print(time)