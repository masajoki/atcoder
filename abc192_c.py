import sys
sys.setrecursionlimit(10**7)
N,K=map(int,input().split())

def cal(n):
    strn=list(str(n))
    strn.sort()
    n2=int("".join(strn))
    strn.reverse()
    n1=int("".join(strn))
    return n1-n2
for i in range(K):
    N=cal(N)

print(N)
