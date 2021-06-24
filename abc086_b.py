a,b=map(int,input().split())
hoge=int(str(a)+str(b))

temp=int(hoge**0.5)

if hoge==temp**2:
    print("Yes")
else:
    print("No")