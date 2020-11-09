import math
A,B,N=map(int,input().split())
ans=0
for i in range(1,A+1):
    temp=(A*i%B)-A*(i%B)
    ans=max(temp,ans)
print(ans)