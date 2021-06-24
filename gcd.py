n,m=map(int,input().split())

def GCD(m,n):
    if n==0:
        return m
    return GCD(n,m%n)

print(GCD(n,m))