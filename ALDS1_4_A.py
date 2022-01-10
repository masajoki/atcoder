import sys

input=sys.stdin.readline
N=int(input())
S=list(map(int,input().split()))
Q=int(input())
T=list(map(int,input().split()))
A=set(S)
ans=0
for t in T:
    if t in A:
        ans+=1
print(ans)
