N,M=map(int,input().split())
A,B,C,T=[],[],[],[]
for i in range(M):
    a,b,c,t=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    T.append(t)

class UnionFind(object):
    def __init__(self, n=1):
        self.parent=[-1 for _ in range(N+1)]
        self.size=[1 for _ in range(N+1)]

    def root(self,x):
        if self.parent[x]==-1:
            return x
        else:
            self.parent[x]=self.root(self.parent[x]) #再帰で根の番号が帰って来る。中間も根に貼り直す。圧縮。
            return self.parent[x]

    def issame(self,x,y):
        return self.root(x)==self.root(y)

    def unite(self,x,y):
        x=self.root(x)
        y=self.root(y)
        if x==y: #x,yが同じグループに所属するかどうか
            return False #同じグループだったらFalseを返す
        if self.size[x]<self.size[y]: #大きいサイズの方に小さいサイズの方をくっつける
            x,y=y,x #size[y]の方を小さくする
        self.parent[y]=x
        self.size[x]+=self.size[y]
        return True #統合が成功したらTrue


uf=UnionFind(N)

cost=[]
for i in range(M):
    cost.append((C[i]/T[i],i))

cost.sort()

allcost=0
allhour=0

mandatory=set()
for i in range(M):
    n=cost[i][1]
    if not uf.issame(A[n], B[n]):
        mandatory.add(n)
        uf.unite(A[n],B[n])
        allcost+=C[n]
        allhour+=T[n]

for c in cost:
    i=c[1]
    if i not in mandatory:
        if c[0]<allcost/allhour:
            allcost+=C[i]
            allhour+=T[i]

print(allcost/allhour)
