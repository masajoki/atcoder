H,W,N=map(int,input().split())
A=[]
As=set()
Ad={}
B=[]
Bs=set()
Bd={}
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    As.add(a)
    B.append(b)
    Bs.add(b)

Asl=list(As)
Asl.sort()
for i in range(len(Asl)):
    Ad[Asl[i]]=i+1

Bsl=list(Bs)
Bsl.sort()
for i in range(len(Bsl)):
    Bd[Bsl[i]]=i+1

for i in range(N):
    print(Ad[A[i]],Bd[B[i]])
    