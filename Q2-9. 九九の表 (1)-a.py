#Q2-9. 九九の表 (1)
#アルゴ式
#二分探索
# https://algo-method.com/tasks/407
N,X=map(int,input().split())

def check(K): #単調増加する式
    anssum=0
    for i in range(1,N+1):
        ans=min(N,K//i)
        anssum+=ans
    return anssum

def is_ok_for_x(arg):
    anssum=check(arg)
    if anssum<X: #X以下ならTrueとして、それより1大きい値を答えにする(?)
        return True
    else:
        return False

#二分探索して、全体の項目数がX以下となるKを返す
def meguru_bisect_for_x(ng,ok):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok_for_x(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans=meguru_bisect_for_x(10**11,0)
print(ans+1)

