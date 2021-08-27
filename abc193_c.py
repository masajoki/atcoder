import math
N=int(input())
n=math.ceil(math.sqrt(N+10))

used=[0 for _ in range(n+1)]

ans=0
for i in range(2,n):
    if used[i]==1:
        continue
    for j in range(2,35):
        if (i**j) <=N:
            ans+=1
            if i**j<=n:
                used[i**j]=1
        else:
            break
print(N-ans)
