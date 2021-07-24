#答えで二分探索
N,L=map(int,input().split())
K=int(input())
A=list(map(int,input().split()))
Cuts=[]

Cuts.append(A[0])
for i in range(N-1):
    Cuts.append(A[i+1]-A[i])
Cuts.append(L-A[N-1])

def is_ok(arg):
    temp=0
    cut=0
    for i in range(N+1):
        temp+=Cuts[i]
        if temp>=arg:
            temp=0
            cut+=1

    if cut>=K+1:
        return True
    return False



def meguru_bisect(ng,ok):

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


ans=meguru_bisect(sum(A),0)

print(ans)