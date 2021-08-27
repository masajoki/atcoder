N,Q=map(int,input().split())
A=list(map(int,input().split()))
L=[]
R=[]
V=[]
H=[0 for _ in range(N+2)] #調整
H2=[0 for _ in range(N+2)] #調整
for i in range(Q):
    l,r,v=map(int,input().split())
    L.append(l)
    R.append(r)
    V.append(v)

Fuben=0
for i in range(N-1):
    Fuben+=abs(A[i+1]-A[i])

for i in range(Q):
    l=L[i]-1
    r=R[i]-1
    if l>0:
        b4=abs(A[l]-A[l-1])
        aft=abs(A[l]+V[i]-A[l-1])
        Fuben=Fuben-b4+aft

    if r<N-1:
        b4=abs(A[r+1]-A[r])
        aft=abs(A[r+1]-A[r]-V[i])
        Fuben=Fuben-b4+aft
    print(Fuben)
