N=int(input())
S=[]
Snon10=[]
for i in  range(N):
    s=int(input())
    S.append(s)
    if s%10!=0:
        Snon10.append(s)
Snon10.sort()
if len(Snon10)==0:
    print(0)
else:
    if sum(S)%10!=0:
        print(sum(S))
    else:
        print(sum(S)-Snon10[0])
