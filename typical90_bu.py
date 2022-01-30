#typical90_bu.py
from collections import deque
N=int(input())
C=list(map(int,input().split()))
AB=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b=map(int,input().split())
    AB[a].append(b)
    AB[b].append(a)

dp=[[0]*2 for _ in range(N+1)]

queue=deque()

