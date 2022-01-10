#Q2-4. 小さい数の個数.py
#アルゴ式
#2分探索
N,M=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split())) 
A.sort()
T=0

def is_ok(X):
    if A[X]>=T:
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

ans=[]
for i in range(M):
    T=B[i]
    a=meguru_bisect(-1,N-1) 
    if A[a]==T:
        ans.append(a)
    else:
        ans.append(a-1)

for a in ans:
    print(a+1)



