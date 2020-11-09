N=int(input())
A=list(map(int,input().split()))
kForMaxGCDDo=0
maxgcdDO=0
for k in range(2,1000+1):
    gcdDO=0

    for a in A:
        if a % k == 0:
            gcdDO+=1
    if maxgcdDO < gcdDO:
        maxgcdDO=gcdDO
        kForMaxGCDDo=k


if kForMaxGCDDo==0:
    print(2)
else:
    print(kForMaxGCDDo)
