N,M,Q=map(int,input().split())
V=[]
W=[]
L=[]
R=[]

for _ in range(N):
    w,v=map(int,input().split())
    W.append(w)
    V.append(v)

X=list(map(int,input().split()))


for _ in range(Q):
    l,r=map(int,input().split())
    L.append(l)
    R.append(r)

VW=[]
for i in range(N):
    VW.append([V[i],W[i]])

VW.sort(reverse=True)

for i in range(Q):
    ans=0
    used=[False for _ in range(N)]

    Xt=[]
    for m in range(M):
        if m<L[i]-1 or R[i]-1<m:
            Xt.append(X[m])
    Xt.sort()
    for xt in Xt:
        for n in range(N):
            if xt>=VW[n][1] and used[n]!=True:
                ans+=VW[n][0]
                used[n]=True
                break
    print(ans)
