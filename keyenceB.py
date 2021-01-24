N,K=map(int,input().split())
A=list(map(int,input().split()))
C=[0 for _ in range(N+1)]

for a in A:
    C[a]+=1

ans=0

maxbox=K
for c in C:
    if c > maxbox:
        ans+=maxbox
    elif c<=maxbox:
        ans+=c
        maxbox=c

print(ans)