N,K=map(int,input().split())
A=list(map(int,input().split()))

A.sort(reverse=True)
ans=0
for i in range(N-1):
    a2=A[i]
    a1=A[i+1]
    d=a2-a1
    if d*(i+1)<=K :
        K-=d*(i+1)
        temp=(a2+a2-d+1)*d//2
        ans+=temp*(i+1)
    elif d*(i+1)>K:
        s=K//(i+1)
        r=K%(i+1)
        if s==1:
            ans+=a2*(i+1)
            K-=(i+1)
        elif s>1:
            temp=(a2+a2-s+1)*s//2
            ans+=temp*(i+1)
            K-=s*(i+1)
        elif s==0:
            for k in range(K):
                ans+=(a2)
            K=0
        for k in range(K):
            ans+=(a2-s)
        K=0


s=min(a1,K//N)
r=0
if a1>K//N:
    r=K//N

temp=(a1+a1-s+1)*s//2
ans+=temp*N
ans+=(a1-s)*r
print(ans)

