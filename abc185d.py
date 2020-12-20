import math
N,M=map(int,input().split())
if M==0:
    print(1)
    exit()
A=list(map(int,input().split()))
A.sort()
G=[]
mingap=999999999999
gap=A[0]-1
if gap>0:
    G.append(gap)

gap=N-A[M-1]
if gap>0:
    G.append(gap)

for i in range(1,M):
    gap=A[i]-A[i-1]-1
    if gap>0:
            G.append(gap)


ans=0
for g in G:
    mingap=min(mingap,g)

for g in G:
    ans+=math.ceil(g/mingap)

print(ans)