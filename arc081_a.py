N=int(input())
A=list(map(int,input().split()))
Adict={}
for a in A:
    if a in Adict:
        Adict[a]+=1
    else:
        Adict[a]=1
cand=[]
for i in Adict.items():
    for j in range(i[1]//2):
        cand.append(i[0])
cand.sort(reverse=True)
if len(cand)>=2:
    print(cand[0]*cand[1])
else:
    print(0)