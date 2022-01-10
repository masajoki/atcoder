#Q2-10. 九九の表 (2)
# https://algo-method.com/tasks/407
#二分探索
#アルゴ式

N,X=map(int,input().split())

A=list(range(1,N+1))


#i行目のK以下の項目数がarg以下ならTrueを返す
def is_ok(arg,i,K):
    temp=A[arg-1]*i
    if temp<=K:
        return True
    else:
        return False

#2分探索して、テーブルのi行のK以下の数を求める
def meguru_bisect(ng,ok,K,i):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid,i,K):
            ok=mid
        else:
            ng=mid
    return ok

anssum=0
def is_ok_for_x(arg):
    anssum=0
    for i in range(1,N+1):
        ans=meguru_bisect(N+1,0,arg,i)
        anssum+=ans
    if anssum<=X:
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
if anssum==X:
    print(ans)
else:
    print(ans+1)



