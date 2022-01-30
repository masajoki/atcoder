#abc235_e.py
#AC回答
#クラスカル
#最小全域木を最初につくらなくてよかった

def main():
    import heapq
    import sys
    input=sys.stdin.readline

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

    N,M,Q=map(int,input().split())
    # ABC=[]
    # ABCq=[]

    # hpq=[]
    hpqall=[]
    # MST=set()
    # uf=UnionFind(N+1)
    uf2=UnionFind(N+1)

    for i in range(M):
        a,b,c=map(int,input().split())
        if a>b:
            a,b=b,a
        # ABC.append((a,b,c,-1))
        # heapq.heappush(hpq,(c,a,b,i))
        heapq.heappush(hpqall,(c,a,b,-1))

    for i in range(Q):
        a,b,c=map(int,input().split())
        if a>b:
            a,b=b,a
        heapq.heappush(hpqall,(c,a,b,i))

    # for i in range(len(hpq)):
    #     c,a,b,i = heapq.heappop(hpq)
    #     if uf.issame(a,b):
    #         continue
    #     else:
    #         uf.unite(a,b)
    #         # MST.add((a,b))

    ans=["No" for _ in range(Q)]

    for _ in range(len(hpqall)):
        c,a,b,i = heapq.heappop(hpqall)
        if not uf2.issame(a,b):
        #     if i!=-1:
        #         ans[i]="No"
        # else:
            if i==-1:
                uf2.unite(a,b)
            else:
                ans[i]="Yes"
    print(*ans)

main()