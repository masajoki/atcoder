X=int(input())
M=int(input())

Xs=str(X)
d=int(max(Xs))

if len(Xs)==1:
    if X<=M:
        print(1)
    else:
        print(0)
    exit()

def is_ok(D):
    global Xs
    temp=0

    for i in range(len(Xs)-1,-1,-1):
        strindex=len(Xs)-1-i
        temp+=(D**i)*int(Xs[strindex])
        if temp>M:
            break
    if temp<=M:
        return True
    else:
        return False


def meguru_bisect(ng, ok):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

temp=meguru_bisect(10**19,1)
if temp<d+1:
    print(0)
else:
    print(temp-d)

#一桁のときの取り扱い
# 2分探索する時に、全部NGな場合があるので広めに探索
# したら解けた。実装ではNGであった。無念。