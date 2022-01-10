# abc233_d
import bisect
N, K = map(int, input().split())

A = [int(i) for i in input().split()]

S = [0] * (N+1)
Scnt = {}
for k in range(1, N+1):
    S[k] = S[k-1] + A[k-1]
    if S[k] in Scnt.keys():
        Scnt[S[k]].append(k)
    else:
        Scnt[S[k]] = [k]

ans = 0
for i in range(N+1):
    if S[i]+K in Scnt.keys():
        sk=Scnt[S[i]+K]
        sklen=len(sk)
        t=sklen-bisect.bisect(sk,i)
        ans+=t
print(ans)
