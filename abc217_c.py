N=int(input())
Pt=list(map(int,input().split()))


Q=[-1 for _ in range(N+1)]
P=[-1 for _ in range(N+1)]

for i in range(1,N+1):
    P[i]=Pt[i-1]
    

for i in range(1,N+1):
    Q[P[i]]=i

for i in range(1,N+1):
    print(Q[i],end=" ")
print()
