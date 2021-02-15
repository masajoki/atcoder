S=input()
T=input()
SD={}
TD={}
abc='abcdefghijklmnopqrstuvwxxyz'

for a in abc:
    SD[a]=0
    TD[a]=0

for i in range(len(S)):
    SD[S[i]]+=1
    TD[T[i]]+=1

SDsorted=sorted(SD.items(),key=lambda x:x[1])
TDsorted=sorted(TD.items(),key=lambda x:x[1])

for i in range(len(SD)):
    if SDsorted[i][1]!=TDsorted[i][1]:
        print("No")
        exit()
print("Yes")
