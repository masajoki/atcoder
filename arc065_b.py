
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

    def getsize(self,x): #xを含むグループのサイズ
        return self.size[self.root(x)]


N,K,L=map(int,input().split())

P,Q,R,S=[],[],[],[]

roadUF=UnionFind(N)

for i in range(K): #ROAD
    p,q=map(int,input().split())
    P.append(p)
    Q.append(q)
    roadUF.unite(p, q)

railUF=UnionFind(N)

for i in range(L): #Rail
    r,s=map(int,input().split())
    R.append(r)
    S.append(s)
    railUF.unite(r, s)


#rootのペアが同一なら同じグループにいるといえる
d={}
for i in range(1,N+1):
    roadRt=roadUF.root(i)
    railRt=railUF.root(i)
    k=(roadRt,railRt)
    if k in d.keys():
        d[k]+=1
    else:
        d[k]=1

for i in range(1,N+1):
    roadRt=roadUF.root(i)
    railRt=railUF.root(i)
    k=(roadRt,railRt)
    print(d[k],end=" ")

print()

