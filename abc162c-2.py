import numpy as np
 
K=int(input())
 
ans=0
for a in range(1,K+1):
    for b in range(1,K+1):
        for c in range(1,K+1):
            ans+=np.gcd(a,c)
print(ans)