#Q2-1. 方程式を解く.py
#アルゴ式
#二分探索
N=int(input())

def is_ok(X):
    X=X/100.0
    temp=X*(X*(X+1)+2)+3-N
    if temp<=0:
        return True
    else:
        return False

def meguru_bisect(ok,ng):
    while (abs( ng - ok )>1):
        mid = (ng + ok ) // 2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans=meguru_bisect(0,10001)
print(ans/100)
