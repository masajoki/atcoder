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

N=int(input())
U,V,W=[],[],[]
uf=UnionFind(N)

#X軸, Y軸それぞれでソートして隣接している都市ごとにコストを計算
import heapq
UVdic={}
UV=[]
path=[[] for _ in range(N+1)]
for i in range(N-1):
    u,v,w=map(int,input().split())
    heapq.heappush(UV,(w,u,v))
    UVdic[(u,v)]=w
    UVdic[(v,u)]=w
    path[u].append(v)
    path[v].append(u)
ans=0

while len(UV)>0:
    w,u,v=heapq.heappop(UV)
    #ループになるならその辺は使わない
    if uf.issame(u,v):
        continue
    else:
        uf.unite(u,v)

ans=0
for i in range(1,N+1):
    iparent=uf.parent[i]
    if iparent!=- 1:
        pathcount=N-uf.size[i]
        w=UVdic[(i,iparent)]
        if pathcount%1==0:
            ans=ans^w

print(ans)        





