N,M=map(int,input().split())
modlist=[ 0 for _ in range(10001)]
repeatbegin=0
repeatend=0
for n in range(1,10000):
    temp1=(10**n)%M
    print(n,temp1)
    if modlist[temp1]!=0:
        print(modlist[temp1],n)
        repeatbegin=modlist[temp1]
        repeatend=n
        break
    modlist[temp1]+=n


reducedN=(N-repeatbegin)%(repeatend-repeatbegin)
ans=( (10**reducedN)%M) //M)%M
print(ans)