N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort()
B.sort()
C.sort()
ans=[]
temp=float("inf")
AB=[]
ABsum=[]

def is_ok(arg, T):
    if T[arg]<temp:
        return True
    else:
        return False

def meguru_bisect(ok, ng, T):
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid, T):
            ok = mid
        else:
            ng = mid
    return ok


for i in range(N):
    temp=B[i]
    if temp<=A[0]:
        a=0
    elif temp> A[-1]:
        a=N
    elif A[0]<temp<A[-1]:
        a=1+meguru_bisect(0, N-1, A)

    AB.append(a)

ABsum.append(AB[0])
for i in range(1,N):
    ABsum.append(ABsum[i-1]+AB[i])

for c in C:
    temp=c
    # b=0
    if temp<=B[0]:
        ans.append(0)
        continue
    elif B[0]<temp<=B[-1]:
        b=meguru_bisect(0, N-1, B)
    elif temp> B[-1]:
        b=N-1
    ans.append(ABsum[b])
print(sum(ans))



