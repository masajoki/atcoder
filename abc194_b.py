N=int(input())
A=[]
B=[]
AminIndex=9999
Amin=9999
BminIndex=9999
Bmin=9999
for i in range(N):
    a,b=map(int,input().split())
    if a<Amin:
        Amin=a
        AminIndex=i
    if b<Bmin:
        Bmin=b
        BminIndex=i
    A.append(a)
    B.append(b)

A.sort()
B.sort()
if AminIndex!=BminIndex:
    print(max(Amin,Bmin))
else:
    a=Amin+Bmin
    b=max(A[0],B[1])
    c=max(A[1],B[0])
    ans=min(a,b,c)
    print(ans)