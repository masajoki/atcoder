# Q2-9. 九九の表 (1)
#二分探索
#アルゴ式
# https://algo-method.com/tasks/406
N,K=map(int,input().split())

A=list(range(1,N+1))


def is_ok(arg,X):
    temp=A[arg-1]*X
    if temp<=K:
        return True
    else:
        return False

def meguru_bisect(ng,ok,X):
    while (abs(ok-ng)>1):
        mid=(ok+ng)//2
        if is_ok(mid,X):
            ok=mid
        else:
            ng=mid
    return ok

ansers=[]
for i in range(1,N+1):
    ans=meguru_bisect(N+1,0,i)
    ansers.append(ans)


# print(*ansers)
print(sum(ansers))


