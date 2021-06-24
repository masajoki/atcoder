N=int(input())
C=[]
P=[]
for i in range(N):
    c,p=map(int,input().split())
    C.append(c)
    P.append(p)
Q=int(input())
L=[]
R=[]
for i in range(Q):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)

Score1=[0 for _ in range(N+1)]
Score2=[0 for _ in range(N+1)]

if C[0]==1:
    Score1[0]=P[0]
else:
    Score2[0]=P[0]

for i in range(1,N):
    if C[i]==1:
        Score1[i]=Score1[i-1]+P[i]
        Score2[i]=Score2[i-1]
    else:
        Score1[i]=Score1[i-1]
        Score2[i]=Score2[i-1]+P[i]

for i in range(Q):
    A,B=0,0
    if L[i]>0:
        A=Score1[R[i]-1]-Score1[L[i]-2]
        B=Score2[R[i]-1]-Score2[L[i]-2]
    else:
        A=Score1[R[i]-1]
        B=Score2[R[i]-1]
    print(A,B)

