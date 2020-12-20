H,W=map(int,input().split())
A= []
for i in range(H):
    a=list(map
    (int,input().split()))
    A.append(a)

mina=999999

for a in A:
    temp=min(a)
    mina=min(mina,temp)

ans=0
for a in A:
    for i in a:
        ans+=i-mina
print(ans)
