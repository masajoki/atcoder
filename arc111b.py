N=int(input())
a=[]
b=[]
colorcount=[0 for i in range(4000001)]
for i in range(N):


    at,bt=map(int,input().split())
    a.append(at)
    b.append(bt)
    if at!=bt:
        colorcount[at]+=1
        colorcount[bt]+=1

ans=0

for i in range(N):
    if colorcount[a[i]]<colorcount[b[i]]:
        if colorcount[a[i]]!=999999999:
            ans+=1
        colorcount[a[i]]=999999999
    elif colorcount[a[i]]>colorcount[b[i]]:
        if colorcount[b[i]]!=999999999:
            ans+=1
        colorcount[b[i]]=999999999
    else:
        if colorcount[b[i]]!=999999999:
            ans+=1
        colorcount[b[i]]=999999999
    


print(ans)
