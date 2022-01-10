import math
N=int(input())
XY=[]
ans=set()
for i in range(N):
    x,y=map(int,input().split())
    XY.append((x,y))

for i in range(N-1):
    for j in range(i+1,N):
        x1,y1=XY[i]
        x2,y2=XY[j]
        gcd1=math.gcd(x2-x1,y2-y1)
        ans.add(((x2-x1)//gcd1,(y2-y1)//gcd1))
        gcd2=math.gcd(x1-x2,y1-y2)
        ans.add(((x1-x2)//gcd2,(y1-y2)//gcd2))

print(len(ans))
