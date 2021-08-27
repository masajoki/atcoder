N=int(input())
L=[]
R=[]
for i in range(N):
    t,l,r=map(int,input().split())
    if t==1:
        L.append(l)
        R.append(r)
    elif t==2:
        L.append(l)
        R.append(r-0.1)
    elif t==3:
        L.append(l+0.1)
        R.append(r)
    elif t==4:
        if l-r!=1:
            L.append(l+0.1)
            R.append(r-0.1)

ans=0
for i in range(N-1):
    for j in range(i+1,N):
        l1=L[i]
        l2=L[j]
        r1=R[i]
        r2=R[j]
        if l1<=l2<=r1 or l1<=r2<=r1 or l2<=l1<=r2 or l2<=r1<=r2:
            ans+=1
print(ans)
