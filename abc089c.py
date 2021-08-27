import itertools
N=int(input())
namecount={}
initials=["M","A","R","C","H"]
for i in initials:
    namecount[i]=0

for i in range(N):
    s=input()
    if s[0] in initials:
        namecount[s[0]]+=1

ans=0
combis=itertools.combinations(initials,3)
for c in combis:
    ans+=namecount[c[0]]*namecount[c[1]]*namecount[c[2]]

print(ans)