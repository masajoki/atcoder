N,L=map(int,input().split())
i=0
ans=0
if L<=-1:
    i=min(1-1*L,N)
elif L>-1:
    i=1

for j in range(1,N+1):
    if j!=i:
        ans+=(j+L-1)
print(ans)