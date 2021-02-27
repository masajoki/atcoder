N,M=map(int,input().split())

P=[]
S=[]
for _ in range(M):
    p,s=input().split()
    P.append(int(p))
    S.append(s)

AC=[0 for _ in range(N+1)]
Pena=[0 for _ in range(N+1)]
for i in range(M):
    if AC[P[i]]==0:
        if S[i]=="AC":
            AC[P[i]]=1
        else:
            Pena[P[i]]+=1

correct=0
pena=0
for i in range(N+1):
    correct+=AC[i]
    if AC[i]==1:
        pena+=Pena[i]

print(correct,pena)



