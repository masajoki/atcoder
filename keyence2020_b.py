N=int(input())
LR=[]
for i in range(N):
    x,l=map(int,input().split())
    LR.append((x-l,x+l))
LR.sort()
maxr=LR[0][1]
ans=1
for l,r in LR:
    if maxr<=l:
        ans+=1
        maxr=r
    elif r<=maxr:
        maxr=r

print(ans)
