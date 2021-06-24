import math
import functools

N,X=map(int,input().split())

A=list(map(lambda x:int(x)-X, input().split()))
ans = functools.reduce(math.gcd, A)
print(abs(ans))