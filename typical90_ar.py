N,Q=map(int,input().split())
A=list(map(int,input().split()))
pad=0
for i in range(Q):
    t,x,y=map(int,input().split())
    if t==1:
        A[x-1+pad],A[y-1+pad]=A[y-1+pad],A[x-1+pad]
    elif t==2:
        pad-=1
    else:
        print(A[x-1+pad])



