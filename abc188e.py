N,M=map(int,input().split())
A=list(map(int,input().split()))
X=[]
Y=[]
path=[[] for _ in range(2*10**5+10)]
for i in range(M):
    x,y=map(int,input().split())
    X.append(x)
    Y.append(y)
    path[x].append(y)

prices=[[0,0] for _ in range(2*10**5+10)]


ans=-999999999999
def route(maxprice,minprice,fromcity):
    global ans
    ans=max(ans,maxprice-minprice)
    for p in path[fromcity]:
        if A[p-1]<minprice:
            minprice=A[p-1]
        if A[p-1]>maxprice:
            maxprice=A[p-1]
        route(maxprice,minprice,p)

route(A[0],A[0],1)
print(ans)