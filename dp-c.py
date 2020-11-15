N=int(input())
a=[]
b=[]
c=[]
dpA=[0 for _ in range(N)] #iに海で泳いだときの最大
dpB=[0 for _ in range(N)] #iに虫とったときの最大
dpC=[0 for _ in range(N)] #iに宿題したときの最大

for i in range(N):
    at,bt,ct=map(int,input().split())
    a.append(at)
    b.append(bt)
    c.append(ct)

dpA[0]=a[0]
dpB[0]=b[0]
dpC[0]=c[0]

for i in range(1,N):
    dpA[i]=max(dpB[i-1]+a[i],dpC[i-1]+a[i])
    dpB[i]=max(dpA[i-1]+b[i],dpC[i-1]+b[i])
    dpC[i]=max(dpA[i-1]+c[i],dpB[i-1]+c[i])

print(max(dpA[N-1],dpB[N-1],dpC[N-1]))


