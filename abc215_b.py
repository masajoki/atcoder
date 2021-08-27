import math
N=int(input())
ans=0
for i in range(70):
    if 2**i<=N:
        ans=max(ans,i)
print(ans)
