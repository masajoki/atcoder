#arc133_a.py
#辞書順がわかってなかった・・・
from collections import Counter, defaultdict
N=int(input())
A=list(map(int,input().split()))
failed=set()
ans=-1
if N==1:
    print()
    exit()
for i in range(N-1):
    if A[i]>A[i+1]:
        ans=A[i]
        break
if i==N-2:
    ans=A[-1]

for a in A:
    if ans==a:
        continue
    else:
        print(a,end=" ")
print()