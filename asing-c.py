import math
N=int(input())
ans=[0]*(N+1)
tempn=0
xmax=int(math.sqrt(N)+1)
for x in range(1,xmax+1):
    ymax=xmax-x
    for y in range(1,xmax+1):    
        zmax=ymax-y
        for z in range(1,xmax+1):
            tempn=((x+y+z)**2-(x*y+y*z+z*x))
            if tempn <= N:
                ans[tempn]+=1
for i in range(1,(N+1)):
    print(ans[i])
