N,K=map(int,input().split())
ans=0
for i in range(2,N-K+1):
    ans+=(K+i-1)*(i-1)
for i in range(N-K+1,2*N-K):
    ans+=(K+i-1)*(i-1)
print(ans)