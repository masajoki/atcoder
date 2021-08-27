N=int(input())
D=list(map(int,input().split()))
DMAX=max(D)
DN=[0 for _ in range(DMAX+1)]
for i in range(N):
    DN[D[i]]+=1

if D[0]!=0:
    print(0)
    exit()
if DN[0]!=1:
    print(0)
    exit()

if 0 in DN:
    print(0)
    exit()
if N==1:
    if D[0]==1:
        print(1)
    else:
        print(0)
    exit()


ans=1
mod=998244353
for i in range(1,DMAX+1):
    ans=(ans*pow(DN[i-1],DN[i],mod))%mod
print(ans)

