N=int(input())
X=[]
Y=[]
R=[]
cross=[]
for i in range(N):
    x,y,r=map(int,input().split())
    cross.append((x*x-r*r+y*y,-1))
    cross.append((x*x+r*r-y*y,+1))
cross.sort()

ans=0
temp=0
for c in cross:
    temp-=c[1]
    ans=max(ans,temp)

print(ans)


