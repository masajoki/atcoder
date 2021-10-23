#064 - Uplift（★3） 

N,Q=map(int,input().split())
A=list(map(int,input().split()))
L=[]
R=[]
V=[]
F=[0 for _ in range(N+2)] #不便さの絶対値を取らない値(A[i+1]-A[i])

fuben=0
for i in range(N-1):
    F[i]=A[i+1]-A[i]
    fuben+=abs(F[i])

for i in range(Q):
    l,r,v=map(int,input().split())
    L.append(l-1)
    R.append(r-1)
    V.append(v)

for i in range(Q):
    r=R[i]
    l=L[i]

    if l>=1:
        fuben-=abs(F[l-1])
        F[l-1]+=V[i]
        fuben+=abs(F[l-1])
    if r!=N-1:
        fuben-=abs(F[r])
        F[r]-=V[i]
        fuben+=abs(F[r])
    print(fuben)
