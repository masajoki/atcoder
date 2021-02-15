mod=10**9+7
n,a,b=map(int,input().split())
temp=pow(2,n,mod)
temp=(temp-1)%mod

def nCrMod(n,r,mod):
    t1=1
    t2=1
    for i in range(r):
        t1=(t1*(n-i))%mod
    for i in range(r,1,-1):
        t2=(t2*r)%mod
    t3=(t1//t2)%mod
    return t3

nCaMod=nCrMod(n,a,mod)
nCbMod=nCrMod(n,b,mod)
print((((temp-nCaMod)%mod)-nCbMod)%mod)