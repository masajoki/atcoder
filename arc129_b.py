#arc129_b
# 3分探索で行けそう→行けなかったけど勉強になった。３分探索一応機能してる。極大だったり極小の値を持つのがどこかを求められる。

Nmax=int(input())
L=[]
Lmin=[]
R=[]
Rmax=[]
lmin=10**10
rmax=0
for i in range(Nmax):
    l,r=map(int,input().split())
    lmin=min(lmin,l)
    rmax=max(rmax,r)
    L.append(l)
    Lmin.append(lmin)

    R.append(r)
    Rmax.append(rmax)


memo={}
def calc(x):
    if (x,N) in memo.keys():
        return memo[(x,N)]
    
    maxdist=0
    for i in range(N):
        l=L[i]
        r=R[i]
        dist=-1
        if x<l:
            dist=l-x
        elif l<=x<=r:
            dist=0
        elif r<x:
            dist=x-r
        maxdist=max(maxdist,dist)
    memo[(x,N)]=maxdist
    return maxdist


def trisect(mi,ma):
    mid1=mi+(ma-mi)//3
    mid2=mi+2*(ma-mi)//3
    dist1=calc(mid1)
    dist2=calc(mid2)
    if mid2-mid1<=1:
        return min(dist1,dist2)
    if dist1<dist2:
        return trisect(mi,mid2)
    elif dist1>dist2:
        return trisect(mid1,ma)
    else:
        return trisect(mid1,mid2)


for N in range(1,Nmax+1):
    ans=trisect(Lmin[N-1]-1,Rmax[N-1]+1)
    print(ans)


pass