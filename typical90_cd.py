#082 - Counting Numbers（★3）
import math

L,R=map(int,input().split())

foldlim=math.floor(math.log10(R))

mod=10**9+7
ans=0
temp=0
for i in range(0,foldlim+1):
    lt=(10**i)
    rt=10**(i+1)-1
    if L > rt:
        continue
    if R < lt:
        continue
    if lt<=L<=rt:
        lt=L
    if lt<=R<=rt:
        rt=R
    
    temp+=(i+1)*(rt-lt+1)*(rt+lt)//2
print(temp%mod)
