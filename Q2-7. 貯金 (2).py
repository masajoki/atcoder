# Q2-7. 貯金 (2).py
# アルゴ式
N=int(input())
X=list(map(int,input().split()))

def is_ok(X,arg):
    temp=(arg+1)*arg//2
    if temp>=X:
        return True
    else:
        return False

def meguru_bisect(X,ng,ok):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(X,mid):
            ok=mid
        else:
            ng=mid
    return ok

for x in X:
    a=meguru_bisect(x,0,10**10)
    print(a)
    


