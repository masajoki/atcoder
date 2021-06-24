#アルゴリズムとデータ構造のp189 参照
# N=int(input())


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
        return self.size(self.root(x))


N,Q=map(int,input().split())
uf=UnionFind(N)
for i in range(Q):
    p,a,b=map(int,input().split())
    if p==0:
        uf.unite(a,b)
    else:
        if uf.issame(a,b):
            print('Yes')
        else:
            print('No')

