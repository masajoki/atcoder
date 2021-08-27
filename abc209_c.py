N=int(input())
C=list(map(int,input().split()))
C.sort()
picked=0
ans=0
mod=10**9+7
for c in C:
    if picked==0:
        picked=1
        ans=c
    else:
        ans=(ans*(c-picked))%mod
        picked+=1
print(ans)
