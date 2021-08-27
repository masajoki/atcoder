W=int(input())
S="DiscoPresentsDiscoveryChannelProgrammingContest2016"
count=0
for s in S:
    if count==W:
        print()
        count=0
    print(s,end="")
    count+=1

if count!=0:
    print()
