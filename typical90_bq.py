#069 - Colorful Blocks 2（★3） 

N,K=map(int,input().split())
mod=10**9+7
if N>=3 and K>=3:
    ans=(K*(K-1)*pow((K-2),N-2,mod))%mod
    print(ans)
elif N>=3 and K<3:
    print(0)
elif N==2 and K>=2:
    ans=(K*(K-1))%mod
    print(ans)
elif N==2 and K<2:
    print(0)
elif N==1 and K>=1:
    print(K%mod)
