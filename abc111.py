import collections
N=int(input())
V=list(input().split())
D={}
Dall={}
for i in range(0,N,2):
    s=V[i]+" "+V[i+1]
    if V[i]!=V[i+1]:
        if s in D:
            D[s]+=1
        else:
            D[s]=1
    
    if s in Dall:
        Dall[s]+=1
    else:
        Dall[s]=1

Dsorted=sorted(D.items(),key=lambda x:x[1],reverse=True)

ans=0
if len(Dsorted)>0:
    v1,v2=Dsorted[0][0].split()
    for d in Dall.items():
        w1,w2=d[0].split()
        if w1!=v1 and w2!=v2:
            ans+=2*d[1]
        elif w1!=v1 or w2!=v2:
            ans+=d[1]
    print(ans)

else:
    print(N//2)