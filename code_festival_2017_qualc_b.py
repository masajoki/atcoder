N=int(input())
A=list(map(int,input().split()))
odds=[]
alls=[]
for a in A:
    # if a in (1,100):
    #     alls.append(2)
    # else:
    alls.append(3)
    if a %2 !=0:
        odds.append(1)
    # elif a ==100:
    #     odds.append(1)
    else:
        odds.append(2)


otemp=1
for o in odds:
    otemp*=o

atemp=1
for a in alls:
    atemp*=a
print(atemp-otemp)