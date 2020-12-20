Nmax,M,T=map(int,input().split())
A=[]
B=[]
for i in range(M):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
N=Nmax
N=N-A[0]
if N<=0:
    print("No")
    exit()
for i in range(M-1):
    N=min(Nmax,B[i]-A[i]+N)
    N-=max(0,A[i+1]-B[i])
    if N<=0:
        print("No")
        exit()
N=min(Nmax,B[M-1]-A[M-1]+N)
N=N-(T-B[M-1])
if N<=0:
    print("No")
else:
    print("Yes")

