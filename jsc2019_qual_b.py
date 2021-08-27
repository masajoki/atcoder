N,K=map(int,input().split())
A=list(map(int,input().split()))
mod=10**9+7
Adict={}
Ascore=[0 for _ in range(N)]
for a in A:
    if a in Adict:
        Adict[a]+=1
    else:
        Adict[a]=1
for i in range(N-1):
    for j in range(i+1,N):
        if A[i]>A[j]:
            Ascore[i]+=1

ans=0

for i in range(N):
    temp=0
    for d in Adict.items():
        if d[0]<A[i]:
            temp+=d[1]
    ans+=temp*(K*(K-1)//2)
    ans+=Ascore[i]*K

print(ans%mod)
