from copy import deepcopy
A=input()
B=input()
S=input()
ABCnt={}
SCnt={}
ABC='abcdefghijklmnopqrstuvwxyz'
for a in ABC:
    ABCnt[a]=0
    SCnt[a]=0

for s in S:
    SCnt[s]+=1
for a in A:
    ABCnt[a]+=1
for b in B:
    ABCnt[b]+=1

ai=0
bi=0


cost=0
Ta=deepcopy(ABCnt)
Tb=deepcopy(ABCnt)

for s in S:
    costA=0
    costB=0
    SCnt[s]-=1
    useA=False
    useB=False

    for i in range(ai,len(A)):
        if A[i]==s:
            costA=i-ai+1
            useA=True
            for i in range(26):
                if SCnt[s]>Ta[s]:
                    useA=False
            break
        else:
            Ta[A[i]]-=1
    
    for j in range(bi,len(B)):
        if B[j]==s:
            costB=j-bi+1
            useB=True
            for i in range(26):
                if SCnt[s]>Tb[s]:
                    useB=False
            break
        else:
            Tb[B[j]]-=1
    
    if useA and useB:
        if costA<costB:
            ai=i+1
            cost+=costA
            Tb=deepcopy(Ta)
        else:
            bi=j+1
            cost+=costB
            Ta=deepcopy(Tb)
    elif useA:
        ai=i+1
        cost+=costA
        Tb=deepcopy(Ta)
    elif useB:
        bi=j+1
        cost+=costB
        Ta=deepcopy(Tb)        
    
print(cost)
    



