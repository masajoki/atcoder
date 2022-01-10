# abc225_d
# 愚直にやるだけ

N, Q = map(int, input().split())
queries = []
E = [-1 for _ in range(N+1)]
P = [-1 for _ in range(N+1)]

for _ in range(Q):
    q = list(map(int, input().split()))
    queries.append(q)


def printConnected(x):
    t = x
    ans = []
    while P[t] != -1:
        t = P[t]
    ans.append(t)
    while E[t] != -1:
        t = E[t]
        ans.append(t)
    print(len(ans), *ans)


for j in range(Q):
    q = queries[j]
    if q[0] == 1:
        x = q[1]
        y = q[2]
        E[x] = y
        P[y] = x
    if q[0] == 2:
        x = q[1]
        y = q[2]
        E[x] = -1
        P[y] = -1
    elif q[0] == 3:
        printConnected(q[1])
