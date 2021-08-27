N=int(input())
T=[]
A=[ 0 for _ in range(N+1)]
Surp=[]


for i in range(N):
    t=int(input())
    T.append(t)
    if A[t]==0:
        A[t]=1
    else:
        Surp.append(t)

for i in range(1,N+1):
    if A[i]==0:
        print(i, Surp[0])
        exit()

