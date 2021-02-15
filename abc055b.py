N=int(input())
ans=1
M=10**9+7
for i in range(1,N+1):
    ans=(ans*i)%M

print(ans)