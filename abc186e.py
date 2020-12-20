T=int(input())
N=[]
S=[]
K=[]
for i in range(T):
    n,s,k=map(int,input().split())
    N.append(n)
    S.append(s)
    K.append(k)

ans=0
for i in range(T):
    n=N[i]
    s=S[i]
    k=K[i]
    if (n-s)%k==0:
        print((n-s)//k)
        continue
    if n%k==0:
        x=0
        if s%2==1:
            print(-1)
            continue
    else:
        for i in range(N):
            if (n*i -s) % k==0:
                print((n*i -s) // k)
                break