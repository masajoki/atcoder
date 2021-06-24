#解説AC
#そうなのかなとは思ったが解答にたどり着きはしなかった

N,Z,W=map(int,input().split())
A=list(map(int,input().split()))
t1=0
t2=0
if N>=2:
    t1=abs(W-A[-1])
    t2=abs(A[-2]-A[-1])
    print(max(t1,t2))
else:
    print(abs(A[0]-W))