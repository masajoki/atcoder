A,B,C=map(int,input().split())
L=[A,B,C]
L.sort()

if L[0]==L[1] and L[1]!=L[2]:
    print("Yes")
elif L[0]!=L[1] and L[1]==L[2]:
    print("Yes")
else:
    print("No")
