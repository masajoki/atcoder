import math
N,H=map(int,input().split())
A=[]
B=[]
maxSlashIndex=-1
maxSlash=-1
Throwable=[]

for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

maxSlash=max(A)
for i in range(N):
    if B[i] > maxSlash:
        Throwable.append(B[i])

Throwable.sort()

ans=0
while len(Throwable)>0 and H>0:
    H-=Throwable.pop()
    ans+=1

if H>0:
    slashed=math.ceil(H/maxSlash)
    ans+=slashed
print(ans)
