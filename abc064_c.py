N=int(input())
A=list(map(int,input().split()))
golds=0
hai=0
cha=0
midori=0
mizu=0
ao=0
ki=0
dai=0
red=0
for a in A:
    if a>=3200:
        golds+=1
    elif 0<a<400:
        hai=1
    elif 400<=a<800:
        cha=1
    elif 800<=a<1200:
        midori=1
    elif 1200<=a<1600:
        mizu=1
    elif 1600<=a<2000:
        ao=1
    elif 2000<=a<2400:
        ki=1
    elif 2400<=a<2800:
        dai=1
    elif 2800<=a<3200:
        red=1
               

minans=max(1,hai+cha+midori+mizu+ao+ki+dai+red)
maxans=hai+cha+midori+mizu+ao+ki+dai+red+golds
print(minans,maxans)    


