import math
A,B=map(int,input().split())
ans=0
for i in range(1,210000):
    t=math.ceil(A/i)
    ta=t*i
    tb=(t+1)*i
    if A<=ta and tb<=B:
        ans=max(ans,i)
print(ans)
