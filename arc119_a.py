N=int(input())
import math
maxb=int(math.log2(N))
ans=[]
for b in range(maxb,-1,-1):
    a=N//2**b
    c=N-2**b*a
    ans.append(a+b+c)

print(min(ans))
