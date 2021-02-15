N=int(input())
S=list(input())

D={}
def initD():
    global D
    for s in S:
        D[s]=0

initD()
ans=0
for i in range(N):
    for s in S[:i]:
        if D[s]==0:
            D[s]=1
    for p in S[i:]:
        if D[p]==1:
            D[p]=2
    temp=0
    for v in D.values():
        if v==2:
            temp+=1
            ans=max(ans,temp)
    initD()

print(ans)

