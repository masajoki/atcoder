import bisect
N,K=map(int,input().split())
#scoreは300まで
Psum=[]
for i in range(N):
    P1,P2,P3=map(int,input().split())
    Psum.append(P1+P2+P3)

PsumSort=sorted(Psum)


for i in range(N):
    bs=Psum[i]+300
    rank=bisect.bisect_right(PsumSort,bs)
    if N-rank+1<=K:
        print("Yes")
    else:
        print("No")