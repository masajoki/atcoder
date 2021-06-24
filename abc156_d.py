n,a,b=map(int,input().split())
mod=10**9+7
allcombi=pow(2,n,mod)

def factmod(n,a,mod):
    acombi=1
    for i in range(n-a+1,n+1):
        acombi=(acombi*i)%mod
    return acombi

def amod(a,mod):
    combi=1
    for i in range(a,-1,-1):
        combi=(combi*i)%mod
    return combi

AC=factmod(n,a,mod)
AM=amod(a,mod)

ACM=(AC*AM)%mod

BC=factmod(n,b,mod)    
BM=amod(b,mod)

BCM=(BC*BM)%mod


ans=(allcombi-ACM)%mod
