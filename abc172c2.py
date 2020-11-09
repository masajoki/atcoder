N,M,K=map(int,input().split())
At=list(map(int,input().split()))
Bt=list(map(int,input().split()))

#０冊を初期値にする
A=[0]
B=[0]


for a in At:
    if A[-1]+a<=K:
        A.append(A[-1]+a)
    else:
        break
for b in Bt:
    if B[-1]+b<=K:
        B.append(B[-1]+b)
    else:
        break

def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    if Ak+B[arg]<=K:
        return True
    else:
        return False


def meguru_bisect(ng, ok):
    '''
    めぐる2分探査
    okはBの冊数たりうる値
    ngはBの冊数たり得ない値を入れる。
    '''

    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


Ak=0

maxBooks=0
for Ai in range(len(A)): 
    Ak=A[Ai]
    Bi=meguru_bisect(len(B),0) #len(B)は配列の要素数として使われるとき最大＋１
    if maxBooks<(Ai+Bi):
        maxBooks=Ai+Bi
print( maxBooks )


