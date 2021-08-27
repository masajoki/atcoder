class UnionFind():
    def __init__(self, n):
        self.parent=[-1 for _ in range(n+1)]
        self.size=[1 for _ in range(n)]

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

H,W=map(int,input().split())
uf=UnionFind(H*W*2)
Q=int(input())
I=[]

for _ in range(Q):
    I.append(list(map(int,input().split())))

def pos(r,c):
    return r*W+c

painted=[[False for _ in range(W+1)] for _ in range(H+1)]
for i in range(Q):
    if I[i][0]==1:
        r,c=I[i][1:]
        painted[r][c]=True
        for t in (-1,1):
            if 1<=r+t<=H and painted[r+t][c]==True:
                uf.unite(pos(r,c),pos(r+t,c))
        for t in (-1,1):
            if 1<=c+t<=W and painted[r][c+t]==True:
                uf.unite(pos(r,c),pos(r,c+t))

    else:
        ra,ca,rb,cb=I[i][1:]
        pa=pos(ra,ca)
        pb=pos(rb,cb)
        if painted[ra][ca]==True and  painted[rb][cb]==True :
            if uf.issame(pa,pb):
                print("Yes")
            else:
                print("No")
        else:
            print("No")


