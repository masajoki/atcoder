N,A,B=map(int,input().split())
X=list(map(int,input().split()))
ans=0
for i in range(N-1):
    if B<A*(X[i+1]-X[i]):
        ans+=B
    else:
        ans+=A*(X[i+1]-X[i])


print(ans)