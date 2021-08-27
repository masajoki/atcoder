N,M=map(int,input().split())
E=[0 for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    if a<b:
        E[b]+=1
    elif b<a:
        E[a]+=1

ans=0
for e in E:
    if e==1:
        ans+=1
print(ans)

