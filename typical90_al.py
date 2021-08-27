import math
A,B=map(int,input().split())
g=math.gcd(A,B)
ans=A*B//g
if ans>10**18:
    print("Large")
else:
    print(ans)