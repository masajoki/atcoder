#アルゴ式.Q2. 約数の個数.py
from collections import defaultdict
A=defaultdict(int)
N=int(input())

for i in range(2,int(N**0.5+1)):
    while N%i==0:
        N//=i
        A[i]+=1
if N!=1:
    A[N]=1
ans=1
for i,c in A.items():
    ans*=(c+1)
print(ans)