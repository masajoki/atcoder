#Q5-5. 粘土の重さ

parent=[]


def init(N):
    parent=[i for i in range(N+1)]
    return parent

def root(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=root(parent[x]) #親を更新しながら経路圧縮
        return parent[x]

def unite(x,y):
    rx=root(x)
    ry=root(y)
    if rx==ry:
        return
    else:
        parent[rx]=ry #xの根rxをyの根ryにつけている

def issame(x,y):
    rx=root(x)
    ry=root(y)
    return rx==ry


N,Q=map(int,input().split())
W=list(map(int,input().split()))
parent=init(N)

T=[]
X=[]
Y=[]
for i in range(Q):
    t,x,y=map(int,input().split())
    T.append(t)
    X.append(x)
    Y.append(y)

for i in range(Q):
    t=T[i]
    x=X[i]
    y=Y[i]
    rx=root(x)
    ry=root(y)
    wx=W[rx]
    wy=W[ry]
    if t==0:
        if not issame(x,y):
            unite(x,y)
        r=root(x)
        if rx!=r:
            W[r]+=wx
        if ry!=r:
            W[r]+=wy
    else:
        r=root(x)
        print(W[r])

