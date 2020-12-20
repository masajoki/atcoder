n=int(input())

def is_ok(arg):
    if (1+arg)*arg//2 <= n+1:
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

saved=meguru_bisect(0,n+1)
print(n-saved+1) 