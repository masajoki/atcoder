N=int(input())
X=list(map(int,input().split()))
xsum=0
xsquaresum=0
for x in X:
    xsum+=x
    xsquaresum+=x**2

X.sort()
ans=999999999999999999
for i in range(X[0],X[-1]+1):
    ans=min(ans,xsquaresum-2*xsum*i+N*i**2)
print(ans)
