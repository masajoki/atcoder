#UNION: 2つの集合を1つの集合に併合する
#find: ある要素がど集合に属しているかを判定する
# union-find はグループの分割はできない。
# 初期状態はすべてが別のグループに所属しているみたいにする

#
# https://atcoder.jp/contests/atc001/tasks/unionfind_a

class UnionFind(object):
    def __init__(self, n=1):
        self.par=[i for i in range(n)]
        self.rank=[0 for _ in range(n)]
        self.size=[1 for _ in range(n)]

    def find(self, x):
        # xが所属するグループを検索する
        if self.par[x]== x:
            return x
        else:
            self.par[x] = self.find(self.par[x])
            return self.par[x]
    
    def union(self, x,y):
        # x と y のグループを結合する
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                x,y=y,x
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1
            self.par[y]=x
            self.size[x]+=self.size[y]
    def is_same(self,x,y):
        return self.find(x)==self.find(y)

    def get_seize(self,x):
        x=self.find(x)
        return self.size[x]

N,Q=map(int,input().split())
uf=UnionFind(N)
for i in range(Q):
    p,a,b=map(int,input().split())
    if p==0:
        uf.union(a,b)
    else:
        if uf.is_same(a,b):
            print('Yes')
        else:
            print('No')



