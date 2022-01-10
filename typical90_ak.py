#typical90_ak.py
#典型 037 - Don't Leave the Spice（★5）

class SegmentTree:
    # https://qiita.com/dn6049949/items/afa12d5d079f518de368
    # 初期化処理
    # f : SegmentTreeにのせるモノイド
    # default : fに対する単位元
    def __init__(self, size, f=lambda x,y : x+y, default=0):
        self.size = 2**(size-1).bit_length() # 簡単のため要素数Nを2冪にする
        self.default = default
        self.dat = [default]*(self.size*2) # 要素を単位元で初期化
        self.f = f

    def update(self, i, x):
        i += self.size
        self.dat[i] = x
        while i > 0:
            i >>= 1
            self.dat[i] = self.f(self.dat[i*2], self.dat[i*2+1])

    def query(self, l, r):
        l += self.size
        r += self.size
        lres, rres = self.default, self.default
        while l < r:
            if l & 1:
                lres = self.f(lres, self.dat[l])
                l += 1

            if r & 1:
                r -= 1
                rres = self.f(self.dat[r], rres) # モノイドでは可換律は保証されていないので演算の方向に注意
            l >>= 1
            r >>= 1
        res = self.f(lres, rres)
        return res
    

W,N=map(int,input().split())
L=[]
R=[]
V=[]

segtree=SegmentTree((W+1)*(N+1),max,0) #単位元はN(何に対してもfしてももとに戻る)
dp=[[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N):
    l,r,v=map(int,input().split())
    L.append(l)
    R.append(r)
    V.append(v)

for i in range(N):
    for w in range(W+1):
        left=max((W+1)*i,(W+1)*i+w-R[i])
        right=max((W+1)*i,(W+1)*i+w-L[i])
        tempmax=segtree.query(left,right+1)
        prev=segtree.query(i*(W+1)+w,i*(W+1)+w+1)
        here=segtree.query((i+1)*(W+1)+w,(i+1)*(W+1)+w+1)
        updatetemp=max(tempmax+V[i],here,prev)
        segtree.update((i+1)*(W+1)+w,updatetemp)

ans=segtree.query(N*(W+1)+W,N*(W+1)+W+1)
if ans==0:
    print(-1)
else:
    print(ans)
