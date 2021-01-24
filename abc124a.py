a,b=map(int,input().split())
if a!=b:
    print(max(a,b)+max(a,b)-1)
else:
    print(a*2)