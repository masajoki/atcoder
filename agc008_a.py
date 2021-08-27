a,b=map(int,input().split())
if a==b:
    print(0)
    exit()
ans=0
if abs(b)>=abs(a):
    if a>0 and b>0:
        print(b-a)
    elif a>0 and b<0:
        print(-b-a+1)
    elif a<0 and b>0:
        print(b+a+1)
    elif a<0 and b<0:
        print(-b+a+2)
    elif a==0 and b<0:
        print(-b+1)
    elif a==0 and b>0:
        print(b)
elif abs(a)>abs(b):
    t=a
    a=b
    b=t
    if a>0 and b>0:
        print(b-a+2)
    elif a>0 and b<0:
        print(-b-a+1)
    elif a<0 and b>0:
        print(b+a+1)
    elif a<0 and b<0:
        print(-b+a)
    elif a==0 and b<0:
        print(-b)
    elif a==0 and b>0:
        print(b+1)
