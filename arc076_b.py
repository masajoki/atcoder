# クラスカル法を利用した。

import heapq

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

N=int(input())
Xn,Yn=[],[]
uf=UnionFind(N)

#X軸, Y軸それぞれでソートして隣接している都市ごとにコストを計算

costheap=[]

for i in range(N):
    x,y=map(int,input().split())
    Xn.append((x,i))
    Yn.append((y,i))

Xn.sort() 
Yn.sort()

for i in range(N-1):
    for A in (Xn,Yn):
        c=abs(A[i+1][0]-A[i][0])
        n1=A[i][1]
        n2=A[i+1][1]  
        heapq.heappush(costheap,(c, n1,n2)) #heapq使ってコストで昇順にする
ans=0

while len(costheap)>0:
    c=heapq.heappop(costheap)
    n1,n2=c[1],c[2]
    #ループになるならその辺は使わない
    if uf.issame(n1, n2):
        continue
    else:
        ans+=c[0]
        uf.unite(n1, n2)
print(ans)

