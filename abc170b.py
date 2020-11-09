x,y=(map(int,input().split()))
s=(4*x-y)/2.0
if s >= 0 and (s*10%10==0) and s <= x:
    print("Yes")
else:
    print("No")

