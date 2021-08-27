#076 - Cake Cut（★3） 
#円形のリストは2つつなげて2分探索

import bisect
N=int(input())
A=list(map(int,input().split()))
A2=A+A

Asum=[]
Total=sum(A)//10
Totalb=sum(A)/10
if Total!=Totalb or Total==0:
    print("No")
    exit()

Asum.append(A2[0])
for i in range(1,len(A2)):
    Asum.append(Asum[i-1]+A2[i])

Alltotal=sum(Asum)

if A2[0]==Total:
    print("Yes")
    exit()

for i in range(len(Asum)-1):
    t=bisect.bisect_left(Asum,Asum[i]+Total)
    if t<len(A2) and Asum[t]-Asum[i]==Total:
        print("Yes")
        exit()
print("No")
