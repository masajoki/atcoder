a,b,c=map(int,input().split())
import math
temp=math.gcd(c,math.gcd(a,b))

ans=(a//temp-1)+(b//temp-1)+(c//temp-1)
print(ans)