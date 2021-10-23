N=int(input()) #max 10**5
A=list(map(int,input().split())) #max 10**9
X=int(input()) #max 10**18
Asum=sum(A)

Xr=X//Asum
Xmod=X%Asum

ans=Xr*N

i=0
while Xmod>=0:
    Xmod-=A[i]
    i+=1
    ans+=1

print(ans)
