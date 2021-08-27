N=int(input())
A=list(map(int,input().split()))
B=[]
absmin=10**9+7
minuscount=0
for a in A:
    if a<0:
        minuscount+=1
    b=abs(a)
    absmin=min(absmin,b)
    B.append(b)

if minuscount%2==0:
    print(sum(B))
else:
    print(sum(B)-absmin*2)

