import math
N=int(input())
R=[]
for i in range(N):
    R.append(int(input()))

R.sort(reverse=True)

ans=0

for i in range(0,len(R),2):
    ans+=R[i]**2*math.pi
for i in range(1,len(R),2):
    ans-=R[i]**2*math.pi
print(ans)