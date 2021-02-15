import itertools
n,d=map(int,input().split())
X=[]
for i in range(n):
    x=list(map(int,input().split()))
    X.append(x)

ans=0
C=list(itertools.combinations(X,2))
for c in C:
    temp=0
    for i in range(d):
        temp+=(c[0][i]-c[1][i])**2

    for i in range(127):
        if temp==i**2:
            ans+=1

print(ans)