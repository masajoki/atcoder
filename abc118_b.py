N,M=map(int,input().split())
K=[]
A=[]
love=[0 for _ in range(M+1)]
for i in range(N):
    a=list(map(int,input().split()))
    K.append(a[0])
    A.append(a[1:])

for t in A:
    for a in t:
        love[a]+=1

ans=0
for l in love:
    if l==N:
        ans+=1

print(ans)
