N=int(input())
P=list(map(int,input().split()))
Pmin=[]
minimum=999999999
for i in P:
    minimum=min(minimum,i)
    Pmin.append(minimum)

ans=0
for i in range(N):
    if Pmin[i] >= P[i]:
        ans+=1

print(ans)

