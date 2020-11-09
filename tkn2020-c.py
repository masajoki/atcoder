#いもす法

import copy
from sys import stdin

n,k=map(int,input().split())
#a=list(map(int,input().split()))
a=list(map(int, stdin.readline().split()))
imosutable=[0]*(n+1)

for m in range(0,k):
    maxed=0
    for i in range(0,n):
        d=a[i]
        imosutable[max(0,i-d)]+=1
        imosutable[min(i+d+1,n)]-=1
    for i in range(1,n):
        imosutable[i]+=imosutable[i-1]
        if imosutable[i]==n:
            maxed+=1   

    if maxed==(n-1) and imosutable[0]==n:
        answer=imosutable[0:n]
        print(' '.join(map(str,answer)))
        exit()

    a=copy.copy(imosutable)
    imosutable=[0]*(n+1)

answer=a[0:n]
for s in answer[0:n-1]:
    print (str(s)+" ",end="")
print(answer[n-1])