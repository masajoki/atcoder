#arc132_c
N,D=map(int,input().split())
MOD=998244353

A=list(map(int,input().split()))
ans=1

for i in range(N):
    cnt=2*D+1-(i+1)
    exempt=[]
    for a in A[max(0,i-D):i+D]:
        if a!=-1:
            exempt.append(a)
            

