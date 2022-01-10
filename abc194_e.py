#この問題Segment Treeでできるかと思ったけど、
# Aに含まれる値が重複しているので
# Aに出現したからといってTreeの値を単位元で更新してはいけない

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
    
N,M=map(int,input().split())
A=list(map(int,input().split()))

segtree=SegmentTree(N,min,N) #単位元はN(何に対してもfしてももとに戻る)

for i in range(N):
    segtree.update(i,i)

for i in range(M):
    segtree.update(A[i],N) #除外するためにNにする

ans=N
for i in range(N-M+1):
    t=segtree.query(0,N)
    ans=min(ans,t)
    segtree.update(A[i],A[i])
    if i+M<N:
        segtree.update(A[i+M],N)

print(ans)




