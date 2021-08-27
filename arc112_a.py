T=int(input())
L=[]
R=[]
for t in range(T):
    left,right=map(int,input().split())
    L.append(left)
    R.append(right)

    
for t in range(T):
    l=L[t]
    r=R[t]
    if r-2*l+1>0:
        print((r-2*l+1)*(r+2*l+2-4*l)//2)
    else:
        print(0)
