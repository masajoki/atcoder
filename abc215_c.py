import itertools
S,Kt=input().split()
Sl=list(S)
Sl.sort()
K=int(Kt)
L=itertools.permutations(Sl)
As=set()
for l in L:
    As.add(l)

Al=list(As)
Al.sort()
temp="".join(Al[K-1])
print(temp)