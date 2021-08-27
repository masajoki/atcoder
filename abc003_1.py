N=int(input())
ans=0
for i in range(1,N+1):
    ans+=i/N*10000
print(int(ans))
