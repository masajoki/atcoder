#アルゴ式.正規化.py

N=int(input())
H=list(map(int,input().split()))
hmin=min(H)
hmax=max(H)
maxdif=hmax-hmin
X=[(h-hmin)/maxdif for h in H]
print(*X)


