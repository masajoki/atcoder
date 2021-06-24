N=int(input())
A=list(map(int,input().split()))
A.sort(reverse=True)
mod=998244353
ans=(sum(list(map(lambda x:x**2, A))))%mod
temp=0
for i in range(N-1):
    temp=(temp*2+A[i])%mod
    ans+=(A[i+1]*temp)%mod
print(ans%mod)
