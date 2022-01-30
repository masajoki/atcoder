#typical90_ak.py
#典型 037 - Don't Leave the Spice（★5）
#セグメントツリーを使う。微妙にうまく動いていないみたいだ。

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

segtree=SegmentTree(W+1,max,0) #単位元は0(何に対してもfしてももとに戻る)
dp=[[0 for _ in range(W+1)] for _ in range(N+1)]


for i in range(N):
    l,r,v=map(int,input().split())
    L.append(l)
    R.append(r)
    V.append(v)



for w in range(W+1):
    if L[0]<=w<=R[0]:
        segtree.update(w,V[0])
        dp[1][w]=V[0]

for i in range(1,N):
    for w in range(W+1):
        left=max(0,w-R[i])
        right=w-L[i]
        if right<1:
            continue
        tempmax=segtree.query(left,right+1)
        if L[i]<=w<=R[i] or tempmax!=0:
            dp[i+1][w]=max(tempmax+V[i],dp[i+1][w])
        dp[i+1][w]=max(dp[i+1][w],dp[i][w])
    for w in range(W+1):
        segtree.update(w,dp[i+1][w])

# print(*dp[N])
if dp[N][W]==0:
    print(-1)
else:
    print(dp[N][W])
