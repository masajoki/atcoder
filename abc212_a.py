a,b=map(int,input().split())
if a>0:
    if b==0:
        print("Gold")
    else:
        print("Alloy")
elif b>0:
    if a==0:
        print("Silver")
    else:
        print("Alloy")