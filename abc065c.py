import math
N,M=map(int,input().split())
double=False

if abs(N-M)>1:
    print(0)
    exit()

double=1
mod=1000000007
monkey=math.factorial(M)
dog=math.factorial(N)
if N==M:
    double=2


ans=((((monkey%mod)*dog)%mod)*double)%mod
print(ans)