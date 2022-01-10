a=list(map(int,list(input())))
b=list(map(int,list(input())))

A=[ 0 for _ in range(10)]
B=[ 0 for _ in range(10)]

for i in a:
    A[i]+=1
for i in b:
    B[i]+=1

ansA=[]
ansB=[]

flag=False
for i in range(1,10):
    j=10-i
    if A[i]>0 and B[j]>0:
        ansA.append(i)
        ansB.append(j)
        A[i]-=1
        B[j]-=1
        Flag=True
        break

if Flag:
    for i in range(1,10):
        j=9-i
        while A[i]>0 and B[j]>0:
            ansA.append(i)
            ansB.append(j)
            A[i]-=1
            B[j]-=1

for k in range(10):
    for i in range(1,10):
        j=k-i
        if j<0:
            j=j+10            
        while A[i]>0 and B[j]>0:
            ansA.append(i)
            ansB.append(j)
            A[i]-=1
            B[j]-=1


pass