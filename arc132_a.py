#arc132_a
N=int(input())
R=list(map(int,input().split()))
C=list(map(int,input().split()))
# IfR=[0 for _ in range(N+1)]
# IfC=[0 for _ in range(N+1)]
# for i in range(N):
#     IfR[R[i]]=i
#     IfC[C[i]]=i

Q=int(input())
Qs=[]
# ans={}
for i in range(Q):
    r,c=map(int,input().split())
    R.append(r)
    C.append(c)
    Qs.append((r,c))


for r,c in Qs:
    t=R[r-1]+C[c-1]
    if t>=1+N:
        print("#",end="")
    else:
        print(".",end="")
print()