#abc232_c
from itertools import permutations
N,M=map(int,input().split())
AB=[]
CD=[]
for i in range(M):
    a,b=map(int,input().split())
    AB.append((a,b))

for i in range(M):
    c,d=map(int,input().split())
    CD.append((c,d))
AB.sort()
CD.sort()

combis=permutations(range(1,N+1),N)
# cmbis=[[3,2,1,4]]
for C in combis:
    T=[]
    for a,b in AB:
        c=C[a-1]
        d=C[b-1]
        if c>d:
            c,d=d,c
        T.append((c,d))
    T.sort()
    if T==CD:
        print("Yes")
        exit()

print("No")
