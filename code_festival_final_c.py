T=int(input())


def calc(arg):
    temp=0
    A=list(str(arg))
    for i in range(len(str(arg))):
        temp+=(arg**i)*int(A[len(A)-1-i])
    return temp

def is_ok(arg):
    temp=calc(arg)
    if temp<=T:
        return True
    else:
        return False

def meguru_bisect(ok,ng):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid):
            ok=mid
        else:
            ng=mid
    return ok

ans=meguru_bisect(10,10001)
if T==calc(ans):
    print(ans)
else:
    print(-1)
