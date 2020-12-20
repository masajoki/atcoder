N,M=map(int,input().split())
A=[0 for _ in range(N+10)]
for i in range(M):
    l,r=map(int,input().split())
    A[l]+=1
    A[r+1]+=-1

ans=0
cards=0
for a in A:
    cards+=a
    if cards==M:
        ans+=1
print(ans)
