N=int(input())
A=list(map(int,input().split()))
A.sort()
Diffs=[A[0]]
for i in range(1,N):
    Diffs.append(A[i]-A[i-1])
mod=10**9+7
ans=1
for i in range(N):
    ans=(ans*(Diffs[i]+1))%mod
print(ans)