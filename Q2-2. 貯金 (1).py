#Q2-2. 貯金 (1).py
#アルゴ式
#二分探索
#少数の二分探索
N,M=map(int,input().split())

def is_ok(X):
    X=X/1000000000
    T=N+1
    for i in range(5):
        T=T*X+1
    if T>=M:
        return True
    else:
        return False

def meguru_bisect(ok,ng):
    while ok-ng>1:
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans=meguru_bisect(20000000000,0)
print(ans/1000000000)
