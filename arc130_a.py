N=int(input())
S=list(input())
counted=[]
lasts=""
count=0
for s in S:
    if s==lasts:
        count+=1
    else:
        counted.append(count)
        count=1
    lasts=s
counted.append(count)

ans=0
for c in counted:
    if c==1:
        pass
    elif c==2:
        ans+=1
    elif c==3:
        ans+=3
    else:
        t=(c*(c-1)//2)
        ans+=t
print(ans)




