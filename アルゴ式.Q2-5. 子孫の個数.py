#アルゴ式.Q2-5. 子孫の個数.py
import sys
sys.setrecursionlimit(10**8)
N=int(input())
P=list(map(int,input().split()))
A=[0 for _ in range(N+1)]
E=[[] for _ in range(N+1)]

def walk(p):
    for v in E[p]:
        A[p]+=walk(v)
    return A[p]+1

for i in range(N-1):
    E[P[i]].append(i+1)

walk(0)
for i in range(N):
    print(A[i])