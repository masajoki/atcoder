N=int(input())
A=list(map(int,input().split()))
if N==1:
    print(A[0])
    exit()
ans=10**10
for b in range(2**(N-1)):
    orList=[]
    orTemp=0
    for c in range(N):
        if (b>>c &1)==1:
            # xor
            orTemp=orTemp|A[c]
            orList.append(orTemp)
            orTemp=0
        else:
            # or
            orTemp=orTemp|A[c]
    orTemp=orTemp|A[c]
    orList.append(orTemp)

    xorTemp=orList[0]
    for o in range(1,len(orList)):
        xorTemp=xorTemp^orList[o]

    ans=min(ans,xorTemp)
print(ans)
