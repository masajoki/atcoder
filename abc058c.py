abc="abcdefghijklmnopqrstuvwxyz"
abcCount={}
abcMin={}
for a in abc:
    abcMin[a]=100

N=int(input())

for n in range(N):
    S=input()
    for a in abc:
        abcCount[a]=0
    for s in S:
        abcCount[s]+=1
    for a in abc:
        abcMin[a]=min(abcMin[a],abcCount[a])

for a in abc:
    if abcMin[a]!=0:
        print(a*abcMin[a],end="")
print()


