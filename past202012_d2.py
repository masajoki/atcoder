N=int(input())
S=[]
for i in range(N):
    S.append(input())

Si=[]
for s in S:
    temp=0
    for c in s:
        if int(c)==0:
            temp-=1
        else:
            break
    Si.append((int(s),temp))

Si.sort(key=lambda x:(x[0],x[1]))

for s in Si:
    n=-1*s[1]
    for i in range(n):
        print("0",end="")

    if s[0]!=0:
        print(str(s[0]))
    else:
        print()


