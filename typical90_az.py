N=int(input())
A=[]
for i in range(N):
    t=list(map(int,input().split()))
    A.append(t)

Ans=[1 for _ in range(6)]

mod=10**9+7
for i in range(6):
    Ans[i]=A[0][i]
for i in range(1,N):
    ts=sum(Ans)
    for j in range(6):
        Ans[j]=(ts*A[i][j])

print(sum(Ans)%mod)