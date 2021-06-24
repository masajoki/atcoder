A,B,C=map(int,input().split())
modset=set()
temp=0
while True:
    temp+=A
    if temp%B==C:
        print("YES")
        break
    elif temp%B in modset:
        print("NO")
        break
    else:
        modset.add(temp%B)


