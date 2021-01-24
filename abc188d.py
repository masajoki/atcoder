import heapq
N,C=map(int,input().split())
A=[]
B=[]

SubDays=set()
CostDict={}

for i in range(N):
    a,b,c=map(int,input().split())
    A.append(a)
    B.append(b)
    SubDays.add(a)
    SubDays.add(b+1)
    if a in CostDict:
        CostDict[a]+=c
    else:
        CostDict[a]=c
    if b+1 in CostDict:
        CostDict[b+1]+=(c*-1)
    else:
        CostDict[b+1]=(c*-1)

SubDays=list(SubDays)
SubDays.sort()

today=0
lastday=0
noPrimeCost=0
realCost=0

totalCost=0
for i in range(len(SubDays)):
    today=SubDays[i]
    days=today-lastday
    if lastday!=0:
        totalCost+=days*realCost
    noPrimeCost+=CostDict[today]
    if noPrimeCost>C:
        realCost=C
    elif noPrimeCost<=C:
        realCost=noPrimeCost
    lastday=today

print(totalCost)


