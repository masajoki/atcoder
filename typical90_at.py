N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))

At=[0 for _ in range(46)]
Bt=[0 for _ in range(46)]
Ct=[0 for _ in range(46)]
for i in range(N):
    At[A[i]%46]+=1
    Bt[B[i]%46]+=1
    Ct[C[i]%46]+=1

ans=0
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46==0:
                ans+=At[i]*Bt[j]*Ct[k]
print(ans)
