N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
csum=0
Plus=[]
Minus=[]
for i in range(N):
    diff=A[i]-B[i]
    C.append(diff)
    csum+=diff
    if diff>0:
        Plus.append(diff)
    elif diff<0:
        Minus.append(diff)

if csum<0:
    print(-1)
    exit()

Plus.sort()
minsum=sum(Minus)
count=0
while minsum<0:
    p=Plus.pop()
    minsum+=p
    count+=1
print(count+len(Minus))

