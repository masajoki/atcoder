N,K=map(int,input().split())
p=list(map(int,input().split()))
pexp=[]
for i in range(N):
    pexp.append((1+p[i])/2)

inimaxexp=0
for i in range(K):
    inimaxexp+=pexp[i]

maxexp=[inimaxexp]
for i in range(N-K):
    inimaxexp=inimaxexp-pexp[i]+pexp[i+K]
    maxexp.append(inimaxexp)
print(max(maxexp))