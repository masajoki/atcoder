from abc import abstractproperty


N,M=map(int,input().split())
A=[]
B=[]
U=[]
D=[]

ruiseki=[0 for _ in range(2*N+2)]
sabun=[0 for _ in range(2*N+2)]

for i in range(M):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)
    if a<b:
        U.append((a,b))
    else:
        D.append((b,a))


