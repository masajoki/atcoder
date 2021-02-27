import itertools
N=int(input())
P=list(map(int,input().split()))
Q=list(map(int,input().split()))
p=0
q=0
permutation=list(itertools.permutations(P,N))

numlist=[]
for i in range(len(permutation)):
    temp=0
    for j in range(N):
        temp+=permutation[i][j]*10**(N-1-j)
    numlist.append(temp)
numlist.sort()

for i in range(N):
    p+=P[i]*10**(N-1-i)
    q+=Q[i]*10**(N-1-i)

pindex=numlist.index(p)
qindex=numlist.index(q)
print(abs(qindex-pindex))