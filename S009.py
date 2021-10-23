import heapq
import itertools
import copy
N=int(input())
S=list(map(int,input().split()))
M=int(input())
R=[]
A=[]

for i in range(M):
    mt=list(map(int,input().split()))
    R.append(mt)

T=[i for i in range(M)]

A.append(S)

tempzero=[0 for _ in range(N)]
Perm=list(itertools.permutations(T))
for perm in Perm:
    tempfrom=copy.deepcopy(S)
    tempto=copy.deepcopy(tempzero)
    for p in perm:
        pattern=R[p]
        for i in range(N):
            tempto[pattern[i]-1]=tempfrom[i]
        tempfrom=copy.deepcopy(tempto)
        tempans=copy.deepcopy(tempto)
        A.append(tempans)
A.sort()
anslist=list(map(str,A[0]))
ans=" ".join(anslist)    
print(ans)
