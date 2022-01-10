#Q2-8. ひもを切る
#二分探索
#小数
#アルゴ式
#https://algo-method.com/submissions/238546

N,K=map(int,input().split())
L=list(map(int,input().split()))

def is_ok(arg):
    arg=arg
    temp=0
    for l in L:
        temp+=l*10000000//arg #10**7倍して考える   
    if temp>=K:
        return True
    else:
        return False

def meguru_bisect(ng,ok):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans=meguru_bisect(10**13,1)
print(ans/10**7)
