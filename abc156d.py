import math
n,a,b=map(int,input().split())

fracta=(math.factorial(n)//(math.factorial(a)*math.factorial(n-a)) )
fractb=(math.factorial(n)//(math.factorial(b)*math.factorial(n-b)) )

ans=1
while n>1000:
    ans=(ans*688423210)%(10**9+7)
    n=n-1000
print(n)

ans=(ans*2**n -1-fracta-fractb) % (10**9+7)
print(ans)