N=int(input())
target=1

def is_ok(arg):
    if N//arg==target:
        return True
    else:
        return False

def meguru_bisect(ok, ng):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok

s=0
i=1
while i<=N:
    target=N//i
    top=meguru_bisect(i,N)
    s+=target*(top-i+1)
    i=top+1

print(s)
