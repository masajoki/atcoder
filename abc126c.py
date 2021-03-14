import math
N,K=map(int,input().split())
ans=0
for n in range(1,N+1):
    if n<=K:
        f=math.ceil(math.log2(K/n))
        ans+=(1/N)*(0.5**f)
    else:
        ans+=(1/N)

print(ans)