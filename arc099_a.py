N,K=map(int,input().split())
A=list(map(int,input().split()))

ans=1
N=N-K
while N>0:
    N=N-K+1
    ans+=1
print(ans)
