S=int(input())

if S<3:
    print(0)
    exit()

ans=0
P=1000000007

def factrialMod(n,mod):
    ans=n
    if n==0:
        ans=1
    while n>1:
        ans=(n-1)*ans%mod
        n-=1
    return ans
for i in range(S//3):
    distributed=S-3*(i+1)    
    B=factrialMod(i+distributed,P)
    A=(factrialMod(i,P)*factrialMod(distributed,P))%P
    ans+=(B*pow(A,P-2,P))%P #フェルマーの小定理
print(ans%P)