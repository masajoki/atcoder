N,K=map(int,input().split())
ans=0
if K>0:
    for i  in range(2+K,2*N+1):
        temp=(N-i+1)*(N-i-K+1)
        ans+=temp
elif K<0:
    for i  in range(2,2*N+K+1):
        temp=(i-1)*(i-2)//2
        ans+=temp
else:
    for i  in range(2,2*N+1):
        temp=(i-1)*(i-2)//2
        ans+=temp

print(ans)