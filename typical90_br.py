import math
N=int(input())
X=[]
Y=[]
for i in range(N):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)

xdsq=0
xsum=sum(X)
xsqsum=sum(list(map(lambda x:x**2,X)))


temp1=4*N*N*xsum*xsum-4*N*xsqsum
if temp1<=0:
    xans=0
    exit()

Xlist=[]
temp=(4*N*N*xsum*xsum-4*N*xsqsum)**0.5
Xlist.append(math.floor((2*N*xsum+temp)/(2*N)))
Xlist.append(math.floor((2*N*xsum-temp)/(2*N)))
Xlist.append(math.ceil((2*N*xsum+temp)/(2*N)))
Xlist.append(math.ceil((2*N*xsum-temp)/(2*N)))

xsummin=10**10
xans=-1
for xt in Xlist:
    xsum=0

    for i in range(N):
        xsum+=abs(X[i]-xt)
    if xsum<xsummin:
        xans=xt

print(xsummin)



xdsq=0
xsum=sum(Y)
xsqsum=sum(list(map(lambda x:x**2,Y)))


temp1=4*N*N*xsum*xsum-4*N*xsqsum
if temp1<=0:
    xans=0
    exit()

Xlist=[]
temp=(4*N*N*xsum*xsum-4*N*xsqsum)**0.5
Xlist.append(math.floor((2*N*xsum+temp)/(2*N)))
Xlist.append(math.floor((2*N*xsum-temp)/(2*N)))
Xlist.append(math.ceil((2*N*xsum+temp)/(2*N)))
Xlist.append(math.ceil((2*N*xsum-temp)/(2*N)))

ysummin=10**10
yans=-1
for xt in Xlist:
    ysum=0

    for i in range(N):
        ysum+=abs(Y[i]-xt)
    if ysum<ysummin:
        yans=xt

print(ysummin)


