v,t,s,d=map(int,input().split())
T=t*v
S=s*v
if T<=d and d<=S:
    print("No")
else:
    print("Yes")