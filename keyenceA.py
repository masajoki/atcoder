A=[]
B=[]
N=int(input())
Amax=[0 for _ in range(N)]
Bmax=[0 for _ in range(N)]
C=[0 for _ in range(N)]

A=list(map(int,input().split()))    
B=list(map(int,input().split()))    
Amax[0]=A[0]
Bmax[0]=B[0]
C[0]=A[0]*B[0]
for i in range(1,N):
    Amax[i]=max(Amax[i-1],A[i])
    Bmax[i]=max(Bmax[i-1],B[i])

print(C[0])
for i in range(1,N):
    candi=max(Amax[i-1]*B[i], A[i]*B[i])
    C[i]=max(C[i-1],candi)
    print(C[i])


