a,b,c=map(int,input().split())
if a==b:
    print(c)
    exit()
elif b==c:
    print(a)
    exit()
elif c==a:
    print(b)
    exit()
else:
    print(0)
    