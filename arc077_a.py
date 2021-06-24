from collections import deque

dq=deque()
N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    if i%2==0:
        dq.append(A[i])
    else:
        dq.appendleft(A[i])

dql=list(dq)
if N%2!=0:
    dql.reverse()

print(*dql)
