N,Q=map(int,input().split())
LR=[0 for _ in range(N+10)]

for i in range(Q):
    l,r=map(int,input().split())
    LR[l]+=1
    LR[r+1]-=1

now=0
for i in range(1,N+1):
    now+=LR[i]
    if now%2==1:
        print(1,end="")
    else:
        print(0,end="")
print()