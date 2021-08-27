N=input()
if len(set(N[1:]))==1 or len(set(N[:3]))==1:
    print("Yes")
else:
    print("No")