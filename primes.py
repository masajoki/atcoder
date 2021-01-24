#N以下の素数列挙
import math
N=int(input())
A=[True for _ in range(N+1)]
for i in range(2,math.floor(math.sqrt(N))+1):
    if A[i]==True:
        for j in range(2,N//i+1):
            if i*j<=N:
                A[i*j]=False
            else:
                break

for i in range(2,N+1):
    if A[i]==True:
        print(i)
