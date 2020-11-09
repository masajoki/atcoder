import math
N=int(input())
X=list(map(int,input().split()))
ans1=0
ans2=0
ans3=0
temp1=0
temp2=0
temp3=[]
for x in X:
    temp1+=abs(x)
    temp2+=x**2
    temp3.append(abs(x))

ans1=temp1
ans2=math.sqrt(temp2)
ans3=max(temp3)

print(ans1)
print(ans2)
print(ans3)