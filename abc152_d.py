import math
N=int(input())
nlen=len(str(N))
n=int(N)

nums=[[0 for _ in range(10)] for _ in range(10)]

for i in range(1,N+1):
    if i<=N:
        s=str(i)
        a=int(s[0])
        b=int(s[-1])
        nums[a][b]+=1

ans=0
for i in range(1,10):
    for j in range(1,10):
        ans+=nums[i][j]*nums[j][i]
print(ans)